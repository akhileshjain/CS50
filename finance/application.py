import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from tempfile import mkdtemp
from datetime import datetime
from passlib.apps import custom_app_context as pwd_context
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Custom filter
app.jinja_env.filters["usd"] = usd
app.jinja_env.globals.update(usd=usd, lookup=lookup, int=int)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.route("/")
@login_required
def home():
    # get user cash total
    result = db.execute("SELECT cash FROM users WHERE id=:id", id=session["user_id"])
    cash = result[0]['cash']

    # pull all transactions belonging to user
    portfolio = db.execute("SELECT stock, quantity FROM portfolio where user_id=:id", id=session["user_id"])

    if not portfolio:
        return apology("sorry you have no holdings", 200)

    grand_total = cash

    # determine current price, stock total value and grand total value
    for stock in portfolio:
        price = lookup(stock['stock'])['price']
        total = stock['quantity'] * price
        stock.update({'price': price, 'total': total})
        grand_total += total

    return render_template("home.html", stocks=portfolio, cash=cash, total=grand_total)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == 'POST':
        if request.form.get("symbol") == '':
            return apology("Please enter a symbol name")
        if request.form.get("shares") == '':
            return apology("Please enter a quantity")
        if int(request.form.get("shares")) < 1 and not request.form.get("shares").isnumeric():
            return apology("Please enter a valid quantity")

        symbol = lookup(request.form.get("symbol"))
        if symbol == None:
            return apology("No such symbol exists")
        else:
            cost = int(request.form.get("shares")) * symbol['price']
            result = db.execute("SELECT cash FROM users WHERE id=:id", id=session["user_id"])
            if cost > result[0]["cash"]:
                return apology("You don't have enough cash")

            db.execute("UPDATE users SET cash=cash-:cost WHERE id=:id", cost=cost, id=session["user_id"]);

            add_transaction = db.execute("INSERT INTO transactions (user_id, stock, quantity, price, date) VALUES (:user_id, :stock, :quantity, :price, :date)",
            user_id=session["user_id"], stock=symbol["symbol"], quantity=int(request.form.get("shares")), price=symbol['price'], date=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

            # pull number of shares of symbol in portfolio
            curr_portfolio = db.execute("SELECT quantity FROM portfolio WHERE stock=:stock and user_id=:id", stock=symbol["symbol"], id=session["user_id"])

            # add to portfolio database
            # if symbol is new, add to portfolio
            if not curr_portfolio:
                db.execute("INSERT INTO portfolio (user_id, stock, quantity) VALUES (:id, :stock, :quantity)",
                    id=session["user_id"], stock=symbol["symbol"], quantity=int(request.form.get("shares")))

            # if symbol is already in portfolio, update quantity of shares and total
            else:
                db.execute("UPDATE portfolio SET quantity=quantity+:quantity WHERE stock=:stock and user_id=:id",
                    id=session["user_id"], quantity=int(request.form.get("shares")), stock=symbol["symbol"]);

            return redirect("/")
    else:
        return render_template("buy.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not pwd_context.verify(request.form.get("password"), rows[0]["hash"]):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # clear portfolio for current user
        db.execute("DELETE from portfolio where user_id=:id", id=session["user_id"])

        # pull all transactions belonging to user and load into portfolio db
        portfolio = db.execute("SELECT stock, SUM(quantity) AS quantity FROM transactions WHERE user_id=:user_id GROUP BY stock ORDER BY stock", user_id=session["user_id"])

        # if portfolio is empty, return to home
        if portfolio:
            for stock in portfolio:
                # calculate current cost of stock
                symbol = stock['stock']
                quantity = stock['quantity']

                db.execute("INSERT INTO portfolio (user_id, stock, quantity) VALUES (:id, :stock, :quantity)",
                    id=session["user_id"], stock=symbol, quantity=quantity)

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    if request.method == "POST":
        symbol = lookup(request.form.get("symbol"))
        if symbol == None:
            return apology("No stock with this symbol")
        else:
            return render_template("quoted.html", result=symbol)
    else:
        """Get stock quote."""
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user."""

    # if user reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username")

        # ensure password and password confirmation were submitted
        elif not request.form.get("password"):
            return apology("must provide password", 400)

        elif not request.form.get("confirmation"):
            return apology("must provide confirm password", 400)

        # ensure password and password confirmation match
        elif request.form.get("password") != request.form.get("confirmation"):
            return apology("password and password confirmation must match", 400)

        # hash password
        hash = pwd_context.hash(request.form.get("password"))

        resultcheck = db.execute("SELECT username FROM users where username = :username", username = request.form.get("username"))

        if resultcheck:
            return apology("username is already registered", 400)

        # add user to database
        result = db.execute("INSERT INTO users (username, hash) VALUES (:username, :hash)", username=request.form.get("username"), hash=hash)

        # remember which user has logged in
        session["user_id"] = result

        # redirect user to home page
        return redirect('/')

    # else if user reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")

@app.route("/history")
@login_required
def history():
    """Show history of transactions."""

    # pull all transactions belonging to user
    portfolio = db.execute("SELECT stock, quantity, price, date FROM transactions WHERE user_id=:id", id=session["user_id"])

    if not portfolio:
        return apology("sorry you have no transactions on record")

    return render_template("history.html", stocks=portfolio)

@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock."""

    # if user reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # ensure stock symbol and number of shares was submitted
        if (not request.form.get("symbol")) or (not request.form.get("shares")):
            return apology("must provide stock symbol and number of shares")

        # ensure number of shares is valid
        if int(request.form.get("shares")) <= 0:
            return apology("must provide valid number of shares (integer)")

        available = db.execute("SELECT quantity FROM portfolio WHERE :stock=stock", stock=request.form.get("symbol"))

        # check that number of shares being sold does not exceed quantity in portfolio
        if int(request.form.get("shares")) > available[0]['quantity']:
            return apology("You may not sell more shares than you currently hold")

        # pull quote from yahoo finance
        quote = lookup(request.form.get("symbol"))

        # check is valid stock name provided
        if quote == None:
            return apology("Stock symbol not valid, please try again")

        # calculate cost of transaction
        cost = int(request.form.get("shares")) * quote['price']

        # update cash amount in users database
        db.execute("UPDATE users SET cash=cash+:cost WHERE id=:id", cost=cost, id=session["user_id"]);

        # add transaction to transaction database
        add_transaction = db.execute("INSERT INTO transactions (user_id, stock, quantity, price, date) VALUES (:user_id, :stock, :quantity, :price, :date)",
            user_id=session["user_id"], stock=quote["symbol"], quantity=-int(request.form.get("shares")), price=quote['price'], date=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

        # update quantity of shares and total
        db.execute("UPDATE portfolio SET quantity=quantity-:quantity WHERE stock=:stock and user_id=:id",
            quantity=int(request.form.get("shares")), stock=quote["symbol"], id=session["user_id"]);

        return redirect('/')
    # else if user reached route via GET (as by clicking a link or via redirect)
    else:
        # pull all transactions belonging to user
        portfolio = db.execute("SELECT stock FROM portfolio where user_id=:id", id=session["user_id"])

        return render_template("sell.html", stocks=portfolio)

def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)

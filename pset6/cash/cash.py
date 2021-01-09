from cs50 import get_float

# Prompt for input while input is not valid
while True:
    cash = get_float("Change owed:")
    if cash > 0:
        break

# Convert dollars to cents
change = round(cash * 100)

# Initialize count
count = 0

# If change is more than 25 cents
if change > 25:
    count += int(change / 25)
    change = change % 25

# If change is less than 25 cents but more than 10 cents
if change >= 10 and change < 25:
    count += int(change / 10)
    change = change % 10

# If change is less than 10 cents but more than 5 cents
if change >= 5 and change < 10:
    count += int(change / 5)
    change = change % 5

# If change is less than 5 cents but more than 1 cent
if change >= 1 and change < 5:
    count += int(change / 1)
    change = change % 1

print(count)
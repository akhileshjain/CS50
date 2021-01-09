def main():
    text = input("Text: ")

    words = len(text.split())
    sentence = text.count('.') + text.count('!') + text.count('?')
    letter = letters(text)

    L = letter / words * 100
    S = sentence / words * 100
    index = round(0.0588 * L - 0.296 * S - 15.8)

    # If Coleman -Lau Index is less than 1, print as below.
    if index < 1:
        print("Before Grade 1")

    # If Coleman -Lau Index is 16 or more, print as below.
    elif index >= 16:
        print("Grade 16+")

    # If Coleman -Lau Index is between 1-16, print as below.
    else:
        print("Grade " + str(index))


def letters(text):
    chars = 0
    for i in range(len(text)):
        if text[i].isalpha():
            chars += 1
    return chars


if __name__ == "__main__":
    main()
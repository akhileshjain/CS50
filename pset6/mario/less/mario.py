from cs50 import get_int

# Check for valid input
while True:
    height = get_int("Height:")
    if height >= 1 and height <= 8:
        break
i = 0
while i < height:
    x = height - 1
    a = 0
    while x > i:
        # Print the required number of spaces
        print(" ", end="")
        x = x - 1
    while a <= i:
        # Print the required number of blocks
        print("#", end="")
        a = a + 1
    # Line breaks
    print()
    i = i + 1

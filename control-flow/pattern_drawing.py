square_length = int(input("Enter the size of the pattern:"))

i = 1
while i <= square_length:
    for _ in range(square_length):
        print("*", end="")  # Print '*' without a newline
    print()  # Move to the next line after printing the row
    i += 1
    
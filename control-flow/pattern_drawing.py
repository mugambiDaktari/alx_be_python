square_length = int(input("Enter the size of the pattern:"))

i = 1
while i <= square_length:
    print(square_length * "*", end="")
    i += 1
    print()
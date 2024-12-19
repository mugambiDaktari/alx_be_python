number = input("Enter a number to see its multiplication table:.")
y = int(number)

for i in range(1, 11):
    product = (i) * y
    print(f"{number} * {i} = {product}")
    
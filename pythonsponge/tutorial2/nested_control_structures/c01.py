num1 = int(input("Enter a positive integer: "))
num2 = int(input("Enter another positive integer: "))

working1 = num1
working2 = num2

while working1 != working2:
    if working1 > working2:
        working1 = working1 - working2
    else:
        working2 = working2 - working1

print("The greatest common divisor of", num1, "and", num2, "is", working1)
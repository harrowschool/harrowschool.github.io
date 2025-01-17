valid = False
while not valid:
    num = input("enter a whole number between 1 and 5 inclusive: ")
    if num.isdigit() and int(num) >=1 and int(num) <= 5:
        valid = True
    else:
        print("invalid")
print("the next number is", int(num) + 1)

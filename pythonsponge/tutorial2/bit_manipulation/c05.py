num = int(input("Enter number: "))

steps = 0
while num != 1:
    steps += 1
    if num % 2 == 0:
        num = num // 2
    else:
        num = num * 3 + 1
    print(num)

print(f"The inputted number took {steps} steps to reach 1.")

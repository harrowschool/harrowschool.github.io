age = int(input())

if age >= 10:
    print("B")
elif age >= 8:
    print("A")
elif age >= 6 and input() == 'Y':
    print("A")
else:
    print("N")

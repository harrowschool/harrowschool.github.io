letter = input("enter a single character: ")
if letter >= 'a' and letter <= 'z':
    print("lowercase")
elif letter >= 'A' and letter <= 'Z':
    print("uppercase")
else:
    print("non-alphabetic")
while True:
    entry = input("enter a non-negative whole number: ")
    if entry.isdigit():
        break
    print("whoops try again...")        
square = int(entry) ** 2
print("the square is", square)
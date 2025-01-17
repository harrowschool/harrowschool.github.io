user_age = 0

def update_age1():
    # BAD PRACTICE METHOD: using global variables
    global user_age
    user_age += int(input("How many years older are you now? "))

def update_age2(age):
    # GOOD PRACTICE METHOD: using parameters & return statement
    new_age = age + int(input("How many years older are you now? "))
    return new_age

while True:
    print("Your age is", user_age)
    print("1. Update age using global variable")
    print("2. Update age using return statement")
    print("3. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        update_age1()
    elif choice == 2:
        # NOTE: we assign the return value back to user_age
        user_age = update_age2(user_age)
    elif choice == 3:
        break
    else:
        print("Invalid choice!")

print("Bye!")

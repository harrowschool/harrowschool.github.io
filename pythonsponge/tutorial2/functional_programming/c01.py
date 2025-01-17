def run_three_times(func):
    for i in range(3):
        # "func" isn't the name of a function, but is a variable which will contain a function
        func()


def say_hello():
    print("Hello world!")


def greet_user():
    name = input("What is your name? ")
    print(f"Hello {name}!")


def say_goodbye():
    print("Goodbye")


# No brackets here
phrase_functions = [say_hello, greet_user, say_goodbye]

print("Enter 1 for a generic greeting, 2 for a personalised greeting, and 3 for a valediction")
option = int(input()) - 1
run_three_times(phrase_functions[option])

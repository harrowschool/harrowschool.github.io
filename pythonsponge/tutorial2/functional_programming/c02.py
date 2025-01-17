def create_printer(string):
    def printer():
        print(string)

    return printer


def get_function_name(func):
    return func.__qualname__


functions = [int, print, len]
option = int(input("Enter the number of a function to use: ")) - 1

___ = functions[option]
name = ___(func)
create_printer(___)__

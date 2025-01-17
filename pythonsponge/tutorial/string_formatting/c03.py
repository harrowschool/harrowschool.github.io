firstname = input("firstname: ")
surname = input("surname: ")
title = input("title: ")

MESSAGE = "I wonder if I should record your details as {2} {0} {1} or just as {2} {1} or maybe even as {1}, {0} ({2})?"

print(MESSAGE.format(firstname, surname, title))
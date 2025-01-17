# SHOPPING LIST EDITOR
# this program uses the os module to check if a file exists
# you can read more aobut it here: https://www.w3schools.com/python/module_os.asp

import os

def make_new_list(list_name):
    items = []
    if os.path.exists(list_name):
        print("That list already exists!")
        return
   
    print("Enter items for your list. Type 'quit' to stop.")

    # ==> TASK 2: change this block to a while loop which ends if the user enters "quit"
    for count in range(3):     
        item = input("Item: ")
        items.append(item)

    file = open(list_name, "w")

    for item in items:
        file.write(item + "\n")

def print_list(list_name):

    if os.path.exists(list_name):
        file = open(list_name, "r")
        shopping_list = file.readlines() # this is a list of strings

        # ==> TASK 3: can you print out each item on a separate line?
        # hint: you might want to use the 'strip()' method to remove the newline character from each item or find another way
        print(shopping_list)

    else:
        print("That list does not exist!")

while True:
    print("Welome to the shopping list program!")
    print("""
    Please select one of the following options by typing the corresponding number:
        1. make new list
        2. print out a list
        9. exit
        """)   
    choice = input("Choice: ")

    if choice == "1":
        list_name = input("Name of list: ")
        make_new_list(list_name)

    elif choice == "2":
        list_name = input("Name of list: ")
        print_list(list_name)

    elif choice == "9":
        break

    # ==>TASK 1: can you make it print an error message if the user enters an invalid choice?


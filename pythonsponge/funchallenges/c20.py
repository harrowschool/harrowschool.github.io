# IGNORE THIS CHECKING BLOCK AND SCROLL DOWN TO TASK 1
def do_check(cond, err_msg, task_name, user):
  if not cond: raise Exception(f"TASK {task_name} ERROR: {err_msg}")
  print(f"{user} EARNT GOLD STAR {task_name}", end="\n\n") # An extra line break to make the output look nice.

____ = 9999

#################
# MAIN PROGRAM
#################

# TASK 1
# TODO type your name below, for example "Francesca" into the MyName variable
# Don't forget to keep the quote marks to keep it as text (a string). This is known as initialising a variable
# THEN RUN the code to get your first star!
MyName = "______"
# With f infront of the quotation marks I can insert the variable MyName in the string using {} to exclude it from the regular string syntax.
task1 = f"my name is {MyName}"
print(task1, end="\n\n")
do_check(MyName != "______", "That's not quite right, add your name into the MyName variable", 1, MyName)

# EXAMPLE
# REMEMBER the first item of a list is at position (index) 0, and the second is index 1 etc...
MyGroceries = ["apples", "pears", "bananas"]
print(f"the second item on my list is {MyGroceries[1]}.", end="\n\n")

# TASK 2:
# HELP, IVE LOST MY GROCERIES SHOPPING LIST! Can you help me find it?: 
# TODO - complete the blank below to include the entire above list in the print out
task2 = f"AHA! I've found your shopping list, it has {____} written on it"  
print(task2, end="\n\n")
do_check("apples" in task2 and "pears" in task2 and "bananas" in task2, "hmm I know that's not my list, try again", 2, MyName)

# TASK 3
# SORRY, I didn't hear what the first item on the list was, could you repeat just that item please?  
# TODO - complete the line below
task3 = f"I'll remind you, your first item was {MyGroceries[____]}"
print(task3, end="\n\n")
do_check("apples" in task3 and "pears" not in task3 and "bananas" not in task3, "hmm I know that's not my list, try again", 3, MyName)

# EXAMPLE
#This is another example of why f-strings are useful:
# this goes through every item in groceries and runs the python below indiviually for each item (you can use any name, in this case I chose 'item')
for item in MyGroceries:
    print(f"I need to get {item}")

print()

# EXAMPLE
MyQuantities = [1, 3, 2]
# I have become very hungry and want 1 more of each fruit. This is how I would use the for __ in __: syntax
MyNewQuantities = []  # this is empty, lets fill it with values.

for number in MyQuantities:
    MyNewQuantities.append(number + 1)   # adds the item to the end of a list. 

print(f"My new quanitites for {MyGroceries} are {MyNewQuantities} respectively", end="\n\n")

# FINAL EXAMPLE!!!:
# round each weight in the list to 2 decimal places
MyGroceryWeights = [1.23452321, 8.233434343, 9.999585351]
print("my item weights to 2dp are: ")
for weight in MyGroceryWeights:
    # this is called a format specifier, it is used to format the output of a variable. 
    # In this case I am rounding to 2 decimal places.
    print(f"{weight:.2f}")

print()
 
# TASK 4
# TODO - print each weight in the list to 4 decimal places instead by completing the blank below
check = True
for number in MyGroceryWeights:
    line = f"{number} rounded to 4 d.p is {____}" 
    print(line)
    check = check and (str(round(number,4)) in line)

print()

do_check(check, "hmm at least one of those output lines isn't right", 4, MyName)

print("WELL DONE!!! ALL STARTS EARNT!")


###########################
# LIBRARY IMPORTS
###########################

import turtle

###########################
# GLOBAL VARIABLES
###########################

myTurtle = turtle.Turtle()
myTurtle.speed(8)

###########################
# MAIN PROGRAM
###########################

# data setup

# use example data for testing
data = '''forward,100
left,90
forward,100
left,90
forward,100
left,90
forward,100'''.splitlines()

# uncomment these two lines to use the real challenge data instead when ready
with open("data.txt", "r") as datafile:
    data = [line.strip() for line in datafile.readlines()]

# setup data
data = [line.split(",") for line in data]


def execute(command):
    action, value = command
    # => COMPLETE THE OTHER INSTRUCTIONS
    if action == "forward":
        turtle.forward(int(value))


for cmd in data:
    # ==> COMPLETE THE NEXT LINE TO CALL THE SUBPROGRAM TO PROCESS THIS COMMAND
    _______(cmd)

# Keep turtle visible
turtle.done()

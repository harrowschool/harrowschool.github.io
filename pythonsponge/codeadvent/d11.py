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

# uncomment these three lines to use the real challenge data instead when ready
# file = open("d11.txt", "r")
# data = [line.strip() for line in file.readlines()]
# file.close()

# setup data
data = [line.split(",") for line in data]

# move turtle to the left of the window to see all of the number
myTurtle.penup()
myTurtle.setposition(-200, 0)
myTurtle.pendown()


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

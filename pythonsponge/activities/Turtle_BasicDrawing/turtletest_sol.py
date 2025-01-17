# LIBRARY IMPORTS
# ==> import the needed library
import turtle

# GLOBAL VARIABLES
sideLength = 20
myTurtle = turtle.Turtle()

# MAIN PROGRAM

# ==> change the pen colour to red
myTurtle.pencolor("red")

# ==> rearrange these lines and complete the gaps
for count in range(3):
  for side in range(4):
    myTurtle.forward(sideLength)
    myTurtle.right(90)
  sideLength += 20

# this line keeps the turtle visible at the end of the program
turtle.done()
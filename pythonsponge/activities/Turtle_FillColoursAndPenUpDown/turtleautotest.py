# LIBRARY IMPORTS
import turtle

# GLOBAL VARIABLES
# ==> create a turtle object called myTurtle
myTurtle = ________________
colours = ["orange", "yellow", "blue"]

# GLOBAL CONSTANTS
RADIUS = 30

# MAIN PROGRAM

# ==> iterate over each colour in the list
for col in _______:

  # ==> set the fill colour to the current list colour
  myTurtle.fillcolor(___)

  myTurtle.begin_fill()
  myTurtle.circle(RADIUS)
  # ==> complete the fill operation
  myTurtle.________()

  # ==> write three lines below to raise the pen, move forward by double the radius and then lower the pen again


# ==> hide the turtle at the end of the animation
myTurtle.__________()

# this line keeps the turtle screen visible at the end of the program
turtle.done()
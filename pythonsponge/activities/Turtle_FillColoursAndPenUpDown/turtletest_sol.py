# LIBRARY IMPORTS
import turtle

# GLOBAL VARIABLES
myTurtle = turtle.Turtle()
colours = ["orange", "yellow", "blue"]

# GLOBAL CONSTANTS
RADIUS = 30

# MAIN PROGRAM

for col in colours:

  myTurtle.fillcolor(col)
  myTurtle.begin_fill()
  myTurtle.circle(RADIUS)
  myTurtle.end_fill()

  myTurtle.penup()
  myTurtle.forward(RADIUS * 2)
  myTurtle.pendown()

# ==> hide the turtle at the end of the animation
myTurtle.hideturtle()

# this line keeps the turtle screen visible at the end of the program
turtle.done()
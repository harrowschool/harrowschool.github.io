import turtle
from random import *

# IGNORE THIS CODE FOR NOW 
# ...AND SCROLL TO THE END FOR THE CHALLENGES

ourTurtle = turtle.Turtle()
ourTurtle.speed(0)
ourTurtle.pendown()
ourTurtle.hideturtle()
ourTurtle.width(4)

racercolours = []
distances = []
ycords = []
____ = ""

def setAmountOfRacers(racerscount):
  if racerscount == "":
    return
  for i in range(racerscount):
    racercolours.append((randint(10, 255),randint(10, 255),randint(10, 255)))
    distances.append(-200)
  for i in range(0,250,int(250/racerscount)):
    ycords.append(100-i)

def race():
  if len(racercolours) == 0:
    return
  while max(distances) < 200:
    for i in range(len(racercolours)):
      ourTurtle.color(racercolours[i])
      ourTurtle.penup()
      ourTurtle.goto(distances[i],ycords[i])
      ourTurtle.pendown()
      distance = randint(0,14)
      ourTurtle.forward(distance)
      distances[i]+=distance
  winner = racercolours[distances.index(max(distances))]
  return winner

def drawStartLine(colour):
  ourTurtle.color(colour)
  ourTurtle.penup()
  ourTurtle.goto(-200,150)
  ourTurtle.pendown()
  ourTurtle.right(90)
  ourTurtle.forward(300)
  ourTurtle.left(90)

def drawFinishLine(colour):
  if colour == "":
    return
  ourTurtle.color(colour)
  ourTurtle.penup()
  ourTurtle.goto(200,150)
  ourTurtle.pendown()
  ourTurtle.right(90)
  ourTurtle.forward(300)
  ourTurtle.left(90)

def circleWinner(winner):
  if winner == "":
    return
  ourTurtle.color(winner)
  ourTurtle.penup()
  ourTurtle.goto(200,ycords[racercolours.index(winner)]-10)
  ourTurtle.pendown()
  ourTurtle.fillcolor(winner)
  ourTurtle.begin_fill()
  ourTurtle.circle(10)
  ourTurtle.end_fill()

# CHALLENGES START HERE

drawStartLine("brown")  # This calls the function called drawStartLine above and passes in the colour brown

# CHALLENGE 1: 
# ==> use the drawfinishline function below to replace the gap and make a golden finish line by passing in the colour as a string
drawFinishLine(____)    

# CHALLENGE 2: 
# ==> choose a number of racers to compete in the race (say 2-5)
setAmountOfRacers(____)

# THIS IS WHERE WE RUN THE RACE AND FIND THE WINNER USING THE race FUNCTION
# The function race returns the winner which we assign to the variable winner. 
winner = race()

# CHALLENGE 3:
# ==> find and call a function that I have written above that can circle the winner by adding a line below
# HINT: you may need to pass in a parameter (like in the previous challenges) to make the function work.

# CHALLENGE 4:
# ==> Change some code above to allow the user to type in how many racers when the program starts

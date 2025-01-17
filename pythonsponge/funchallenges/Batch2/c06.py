import random
import turtle

NUM_GOES = 3
ERROR_FACTOR_MIN = 0.9
ERROR_FACTOR_MAX = 1.1

myTurtle = turtle.Turtle()
myTurtle.penup()
myTurtle.setposition(0,-190)
myTurtle.pendown()
myTurtle.pencolor("red")

challenges = sorted([random.randint(50,150) for count in range(NUM_GOES)])

for size in challenges:

  myTurtle.circle(size)
  guess = input("Look at the canvas then guess the radius in pixels: ")
  if guess.isdigit():
    error_factor = int(guess) / size
    if ERROR_FACTOR_MIN <= error_factor <= ERROR_FACTOR_MAX:
      print("Yay, close enough, you score a point ... it was... ", size)
    else:
      print("Hmmm, not quite good enough ... it was... ", size)
  
print("Game over: hope you liked it!")
  
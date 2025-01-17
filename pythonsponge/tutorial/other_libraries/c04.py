import turtle
import random

STEPS = 12
ARM_LENGTH = 60
COLS = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

pet = turtle.Turtle()

for count in range(STEPS):
  pet.forward(ARM_LENGTH)
  if count % 2 == 0:
    # pick a random color from the list  
    pet.fillcolor(random.choice(COLS))
    pet.begin_fill()
    pet.circle(10)
    pet.end_fill()
  pet.setposition(0, 0)
  pet.right(360 // STEPS)

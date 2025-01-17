import turtle

SIDES = 6
SIDE_LENGTH = 80

pet = turtle.Turtle()

for count in range(SIDES):
  pet.forward(SIDE_LENGTH)
  pet.right(360 // SIDES)
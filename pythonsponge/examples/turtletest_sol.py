# LIBRARY IMPORTS

import turtle

n = int(input("enter length of sides: "))

turtle.pencolor("red")
for _ in range(4):
    turtle.forward(n)
    turtle.right(90)

turtle.done()

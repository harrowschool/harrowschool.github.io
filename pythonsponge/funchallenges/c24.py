from turtle import *

# defining and setting the starting position of our turtle.
t = Turtle()
t.penup()
t.goto(0, -100)
t.pendown()
t.left(90)

# setting the speed
t.speed(9)


def tree(size, levels, angle):
    # when we reach the end of a branch, we change the colour and draw a circle, like a 'leaf'
    if levels == 0:
        t.color("green")
        t.right(90)
        t.circle(size)
        t.left(90)
        t.color("black")
        return

    # moving forward then turning right by a certain angle
    t.forward(size)
    t.right(angle)

    # creating 2 smaller splitting branches
    tree(size * 0.7, levels - 1, angle)
    t.left(angle * 2)
    tree(size * 0.7, levels - 1, angle)

    t.right(angle)
    t.backward(size)


# calling our tree function to draw it!
tree(50, 5, 30)

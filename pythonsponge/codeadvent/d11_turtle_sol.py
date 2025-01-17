import turtle

# Function to draw a digit using a list of commands


def execute(commands):
    for command in commands:
        action, value = command
        if action == "forward":
            turtle.forward(value)
        elif action == "left":
            turtle.left(value)
        elif action == "right":
            turtle.right(value)
        elif action == "pen up":
            turtle.penup()
        elif action == "pen down":
            turtle.pendown()


commands = [["pen down", None], ["forward", 50], ["right", 125], ["forward", 75], ["pen up", None], ["left", 180], ["forward", 75], ["right", 55], ["forward", 30], ["pen down", None], ["forward", 50], ["right", 90], ["forward", 30], ["right", 90], ["forward", 50], ["left", 90], ["forward", 30], ["left", 90], ["forward", 50], ["left", 90], ["pen up", None], ["forward", 60], ["right", 90], ["forward", 30], ["pen down", None], ["forward", 50], ["right", 90], ["forward", 30], ["right", 90], ["forward", 50], ["left", 90], ["forward", 30], ["left", 90], ["forward", 50], ["left", 90], ["forward", 30], ["left", 90], ["forward", 50], ["right", 90], [
    "forward", 30], ["right", 90], ["pen up", None], ["forward", 80], ["forward", 25], ["right", 90], ["pen down", None], ["forward", 60], ["right", 90], ["forward", 15], ["left", 180], ["forward", 30], ["left", 180], ["forward", 15], ["right", 90], ["forward", 60], ["left", 135], ["forward", 15], ["right", 180], ["forward", 15], ["right", 45], ["pen up", None], ["forward", 55], ["pen down", None], ["forward", 50], ["right", 180], ["forward", 50], ["left", 90], ["forward", 30], ["left", 90], ["forward", 50], ["right", 90], ["forward", 30], ["right", 90], ["forward", 50], ["right", 180], ["pen up", None], ["forward", 80]]

# Setup Turtle
# move turtle to the left of the window to see all of the number
turtle.penup()
turtle.setposition(-200, 0)
turtle.pendown()

turtle.speed(1)

execute(commands)

turtle.done()

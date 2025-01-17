import turtle


class Rectangle:
  COLOURS = {
      "red": "#fe0000",
      "green": "#00fe00",
      "blue": "#0000fe"
  }

  def __init__(self, x1, y1, x2, y2, colour_name):
    self.x1 = x1
    self.y1 = y1
    ___.length = x2 - x1
    ____ = ___
    ____ = Rectangle.COLOURS[___]

    ___

  def draw(self):
    turtle.penup()
    turtle.pencolor(self.colour)
    turtle.goto(self.x1, self.y1)
    turtle.pendown()
    turtle.seth(0)
    turtle.forward(self.length)
    turtle.right(90)
    turtle.forward(self.height)
    turtle.right(90)
    turtle.forward(___)
    turtle.right(90)
    turtle.forward(___)
    turtle.done()


rectangle1 = Rectangle(-30, 30, 100, 100, "green")
rectangle2 = Rectangle(60, -10, 20, 20, "red")

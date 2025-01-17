from turtle import Turtle

# DON'T CHANGE ANY OF THIS UNTIL FINAL EXTENSION
SIZE = 40
COLOUR = "red"
LENGTH = 3
t = Turtle()
t.pencolor(COLOUR) 

###########################
# DON'T CHANGE ANY OF THIS
# Scroll down to the challenges area
###########################

t.hideturtle()
t.penup()
t.speed(0)
t.width(2)
grid = [[" "] * LENGTH for _ in range(LENGTH)]
gameOver = False

def checkGameOver(x, y, turn):
  check = "OX"[turn]
  checkLi = [check] * LENGTH
  if x == y: 
    #checking diagonals
    if [grid[j][j] for j in range(LENGTH)] == checkLi:
      return True
  if x + y == LENGTH + 1:
    if [grid[LENGTH-j-1][j] for j in range(LENGTH)] == checkLi:
      return True
  if grid[y-1] == checkLi:
    return True
  if [grid[j][x-1] for j in range(LENGTH)] == checkLi:
    return True
  return False

def isEmpty(x, y):
  return grid[y-1][x-1] == " "

def isDraw():
  return not sum(" " in grid[j] for j in range(LENGTH))

def drawCross(x, y):
  grid[y-1][x-1] = "X"
  crossx, crossy = (x - LENGTH / 2 - 0.5) * SIZE, (y - LENGTH / 2 - 0.5) * SIZE
  const = SIZE * (1.28 ** 0.5)
  t.goto(crossx - SIZE * 0.4, crossy - SIZE * 0.4)
  t.pendown()
  t.left(45)
  t.forward(const)
  t.penup()
  t.right(90)
  t.goto(crossx - SIZE * 0.4, crossy + SIZE * 0.4)
  t.pendown()
  t.forward(const)
  t.penup()
  t.left(45)
  return checkGameOver(x, y, True)

def drawCircle(x, y):
  grid[y-1][x-1] = "O"
  crossx, crossy = (x - LENGTH / 2 - 0.5) * SIZE, (y - LENGTH / 2 - 0.5) * SIZE
  t.goto(crossx, crossy - SIZE * 0.4)
  t.pendown()
  t.circle(SIZE * 0.4)
  t.penup()
  return checkGameOver(x, y, False)

def drawGrid():
  halfLen = LENGTH / 2
  for i in range(LENGTH + 1):
    t.goto(-halfLen * SIZE, SIZE * (i - halfLen))
    t.pendown()
    t.forward(SIZE * LENGTH)
    t.penup()
    t.goto(SIZE * (i - halfLen), -SIZE * halfLen)
    t.left(90)
    t.pendown()
    t.forward(SIZE * LENGTH)
    t.penup()
    t.right(90)
  t.goto(0, 0)

drawGrid()
crossesTurn = True

###########################
# CHALLENGE AREA
# Make changes to the main game loop below
###########################

while True:

  if crossesTurn:
    print("X's turn!")
  else:
    print("O's turn!")
    
  coordinates = input(f"Input x and y coordinates from 1,1 to 3,3: ")
  x, y = [int(n) for n in coordinates.split(",")]
  
  # CHALLENGE 1
  # Stop the user from placing outside of the grid
  # We need to make sure their x and y choice are both between 1-3 inclusive
  # Change the True in the next if line to a boolean condition that checks this
  
  # CHALLENGE 2
  # We further need to adapt this if condition to also check that the square is empty
  # you can use the isEmpty function above to do this
  
  # change the next line to check for valid move
  if True:
  
    if crossesTurn: 
        gameOver = drawCross(x,y)
    else:
        gameOver = drawCircle(x,y)
        
    crossesTurn = not crossesTurn
    
    # check for winner
    if gameOver:
      winner = "XO"[crossesTurn]
      print("winner is: ", winner) 
      break
      
    # CHALLENGE 3
    # we also need to check for a draw
    # add similar code to the last 4 lines of code but you can use the isDraw function

input("GAME OVER...press enter to finish...")

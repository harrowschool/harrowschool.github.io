# MINESWEEPER

############################
# SCROLL DOWN FOR MAIN TASKS
############################

from random import randrange
from collections import deque

GRIDSIZE = 8
TRANSFORMS = [(-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1)]

# ==> Extension task!  (save for the end)
# Can you figure out how to show  row & column numbers on the printed grid by editing the function below
def drawGrid(grid, visible, flags):
  print("-"*(2*GRIDSIZE+3))
  for row in range(GRIDSIZE):
    nLine = "| "
    for col in range(GRIDSIZE):
      ch = ""
      if (row,col) in flags:
        ch = "X"
      elif (row,col) in visible:
        if grid[row][col]>0: ch=str(grid[row][col])
        elif grid[row][col]==0: ch=" "
        else: ch = "!"
      else:
        ch="#"
      nLine+=ch+" "
    print(nLine+"|")
  print("-"*(2*GRIDSIZE+3))

#################################################
# DON'T EDIT BELOW - SCROLL DOWN FOR MAIN TASKS
#################################################

def generateGrid():
  grid = [[0 for _ in range(GRIDSIZE)] for _ in range(GRIDSIZE)]
  maxMines = int(0.3*(GRIDSIZE**2))
  k = list(range(GRIDSIZE**2))
  emptyCells = set([ (c//GRIDSIZE,c%GRIDSIZE) for c in k ])
  for j in range(maxMines):
    nInd = randrange(0,len(k))
    nVal = k.pop(nInd)
    y,x = nVal//GRIDSIZE,nVal%GRIDSIZE
    grid[y][x] = -1
    emptyCells.remove((y,x))
    for i in TRANSFORMS:
      if 0<=y+i[0]<GRIDSIZE and 0<=x+i[1]<GRIDSIZE:
        if grid[y+i[0]][x+i[1]]>-1:
          grid[y+i[0]][x+i[1]]+=1
  return grid, emptyCells

def revealStartSquares(grid,startRow,startColumn):
  visible = set()
  q = deque([(startRow,startColumn)])
  while q:
    item = q.popleft()
    visible.add(item)
    if grid[item[0]][item[1]]==0:
      for i in TRANSFORMS:
        nextPos = (item[0]+i[0],item[1]+i[1])
        if 0<=nextPos[0]<GRIDSIZE and 0<=nextPos[1]<GRIDSIZE:
          if not nextPos in visible:
            q.append(nextPos)
  return visible

#################################################
# MAIN PROGRAM - TASKS START BELOW
#################################################

grid, emptyCells = generateGrid()
flags = set()
visible = set()

for r,row in enumerate(grid):
  for c,col in enumerate(row):
    if col==0:
      visible = revealStartSquares(grid,r,c)
      break

emptyCells -= visible

while True:
  drawGrid(grid,visible,flags)
  if len(emptyCells) == 0:
    print("Well done!")
    # ==> Task 1
    # there are no empty squares left (that don't have mines)
    # this means that the game has been won
    # can you end the game by quitting the loop? 

  # ==> Task 3
  # can you apply validation to the two inputs below
  # so that it uses a while loop to ask for an x value UNTIL it is between 1 and GRIDSIZE? 
  # ...and then the same for y?
  # hint: see below for how this has been done with the flag choice input
  
  column = int(input(f"Input the column to check (1-{GRIDSIZE}):")) - 1
  row = int(input(f"Input the row to check (1-{GRIDSIZE}):")) - 1
  
  while True:
    flag = input("Reveal the square or place a flag (r/f):")
    if flag == "r" or flag == "f":
      break
    print("invalid choice ... try again...")

  if flag == "f":
    flags.add( (row,column) )
  elif flag == "r":
    # ==> Task 4
    # currently if you try to reveal where you previously put a flag then the flag marker still remains
    # can you check if (row,column) is in flags and remove it if so before making the square visible?
    visible.add( (row,column) )
    if grid[row][column] == -1:
      print("Game over!")
      # ==> Task 2
      # if grid[y][x] is equal to -1, we hit a mine and the game is over
      # can you show the grid and then end the game?
    else:
      emptyCells.remove( (row,column) )



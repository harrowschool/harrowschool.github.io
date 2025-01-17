from sys import stdctx
from dataclasses import dataclass
from math import pi
import time

##################
# GAME OBJECTS
##################

@dataclass
class Car:
    column: int = 0
    row: int = 0
    xDir: int = 0
    isCrashed: bool = False

#############
# CONSTANTS
############

SCREEN_HEIGHT = 400
SCREEN_WIDTH = 500
CELL_WIDTH = 40
GRID_SIZE = 6
Y_OFFSET = 50
X_OFFSET = 50
PAUSE_TIME = 0.2
##############
# GLOBAL VARIABLES
##############

# the main car object
car = Car()

gameOver = False

#############
# SUBPROGRAMS
#############

def drawCar(x, y):
  # car body
  stdctx.beginPath()
  stdctx.moveTo(x+3, y+30)
  stdctx.lineTo(x+37, y+30)
  stdctx.lineTo(x+37, y+20)
  stdctx.quadraticCurveTo(x+34, y+16, x+30, y+15)  
  stdctx.lineTo(x+25, y+10)
  stdctx.lineTo(x+12, y+10)
  stdctx.lineTo(x+8, y+17)
  stdctx.lineTo(x+3, y+17)
  stdctx.closePath()
  stdctx.fillStyle = "red"
  stdctx.fill()
  # car window 1
  stdctx.beginPath()
  stdctx.moveTo(x+14, y+12)
  stdctx.lineTo(x+19, y+12)
  stdctx.lineTo(x+19, y+16)
  stdctx.lineTo(x+11, y+16)
  stdctx.closePath()
  stdctx.fillStyle = "white"
  stdctx.fill()
  # car window 2
  stdctx.beginPath()
  stdctx.moveTo(x+21, y+12)
  stdctx.lineTo(x+25, y+12)
  stdctx.lineTo(x+29, y+16)
  stdctx.lineTo(x+21, y+16)
  stdctx.closePath()
  stdctx.fillStyle = "white"
  stdctx.fill()
  # car wheel 1
  stdctx.beginPath()
  stdctx.arc(x+12, y+30, 6, 0, pi * 2)
  stdctx.fillStyle = "white"
  stdctx.fill()
  stdctx.beginPath()
  stdctx.arc(x+12, y+30, 4, 0, pi * 2)
  stdctx.fillStyle = "red"
  stdctx.fill()     
  # car wheel 2
  stdctx.beginPath()
  stdctx.arc(x+28, y+30, 6, 0, pi * 2)
  stdctx.fillStyle = "white"
  stdctx.fill()
  stdctx.beginPath()
  stdctx.arc(x+28, y+30, 4, 0, pi * 2)
  stdctx.fillStyle = "red"
  stdctx.fill() 

def drawBorder(x, y):
  stdctx.strokeStyle = "black"
  stdctx.strokeRect(X_OFFSET + x * CELL_WIDTH, Y_OFFSET + y * CELL_WIDTH, CELL_WIDTH, CELL_WIDTH)  

def drawTrackSquare(x, y):
  stdctx.fillStyle = "#FFFFFF"
  stdctx.fillRect(X_OFFSET + x * CELL_WIDTH, Y_OFFSET + y * CELL_WIDTH, CELL_WIDTH, CELL_WIDTH)
  drawBorder(x, y)

def drawCarSquare(x, y):
  drawCar(X_OFFSET + x * CELL_WIDTH, Y_OFFSET + y * CELL_WIDTH)
  drawBorder(x, y)

def doPause():
  start = time.time()
  while time.time() - start < PAUSE_TIME:
    checkKeys()

def drawTrack():
  for x in range(GRID_SIZE):
    drawTrackSquare(x, 0)
  drawCarSquare(car.column, car.row)
    
def resetScreen():
  stdctx.fillStyle = "#D0D0D0"
  stdctx.fillRect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)

def checkKeys():
  if stdctx.check_key(39):
    car.xDir = 1
  elif stdctx.check_key(37):
    car.xDir = -1
  
def checkCrash():
  if car.column < 0 or car.column >= GRID_SIZE:
    return True
  return False

def animate():
  drawTrackSquare(car.column, car.row)
  car.column += car.xDir
  car.isCrashed = checkCrash()
  if car.isCrashed:
    return True
  else:
    drawCarSquare(car.column, car.row)
    stdctx.present()  

resetScreen()
drawTrack()
stdctx.present()

while not gameOver:
    doPause()
    gameOver = animate()  

stdctx.fillStyle = "blue"
stdctx.fillText("GAME OVER: SADLY, YOU HAVE CRASHED!!", 10, 20)
stdctx.present()
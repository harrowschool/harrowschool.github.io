from sys import stdctx
from time import sleep
from math import pi

##################
# GAME OBJECTS
##################

class Board:

  BOARD_HEIGHT = 6
  BOARD_COLS = 7
  PIECE_COLOURS = ["#FF0000", "#0000FF"]

  def __init__(self):
    self._columns = [[] for _ in range(Board.BOARD_COLS)]
    self._turn = 0
    self._col = 0 # for current active column

  def play(self):
    # use 0 and 1 for player 0 and player 1 respectively
    if len(self._columns[self._col]) < Board.BOARD_HEIGHT:
      self._columns[self._col].append(self._turn)
      self._turn = 1 - self._turn
    else:
      raise IndexError('game column is full')

  def get_cell(self, row, col):
    if len(self._columns[col]) > row:
      return self._columns[col][row]
    else:
      # use -1 for empty cell
      return -1

  def slide_col(self, change):
    self._col = min(max(self._col + change, 0), Board.BOARD_COLS - 1)

  @property
  def col(self):
    return self._col

  @property
  def game_over(self):
    return False

  @property
  def piece_colour(self):
    return Board.PIECE_COLOURS[self._turn]

#############
# CONSTANTS
############

SCREEN_HEIGHT = 400
SCREEN_WIDTH = 500
CELL_WIDTH = 50
Y_OFFSET = 50
X_OFFSET = 50
PAUSE_TIME = 0.2
MARKER_SIZE = 10
MOVE_DELAY = 0.2
BORDER_COLOUR = "#000000"
BACK_COLOUR = "#F0F0F0"

##############
# GLOBAL VARIABLES
##############

board = Board()

##############
# SUBPROGRAMS
##############

def draw_marker(col):
  stdctx.fillStyle = board.piece_colour
  x_pos = X_OFFSET + col * CELL_WIDTH + (CELL_WIDTH - MARKER_SIZE) // 2
  stdctx.fillRect(x_pos, Y_OFFSET // 2, MARKER_SIZE, MARKER_SIZE)

def draw_cell(row, col, piece):
  stdctx.strokeStyle = BORDER_COLOUR
  top_left = X_OFFSET + col * CELL_WIDTH
  top_right = Y_OFFSET + row * CELL_WIDTH
  stdctx.strokeRect(top_left, top_right, CELL_WIDTH, CELL_WIDTH)

  if piece >= 0:
    stdctx.fillStyle = Board.PIECE_COLOURS[piece]
    stdctx.beginPath()
    stdctx.arc(top_left + CELL_WIDTH // 2, top_right + CELL_WIDTH // 2, CELL_WIDTH // 2 * 0.9, 0, pi * 2, True)
    stdctx.fill() 

def reset_screen():
  stdctx.fillStyle = BACK_COLOUR
  stdctx.fillRect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)

def update():
  reset_screen()
  draw_marker(board.col)
  for row in range(Board.BOARD_HEIGHT):
    for col in range(Board.BOARD_COLS):
      draw_cell(Board.BOARD_HEIGHT - row - 1, col, board.get_cell(row, col))
  stdctx.present()  

def get_key():
  # left, right to move with down arrow to play
  while True:
    if stdctx.check_key(39):
      board.slide_col(1)
      return
    elif stdctx.check_key(37):
      board.slide_col(-1)
      return
    elif stdctx.check_key(40):
      try:
        board.play()
        return 
      except:
        pass         

##############
# MAIN
##############

update()

# main game loop
while not board.game_over:
    get_key()
    update()
    sleep(MOVE_DELAY)

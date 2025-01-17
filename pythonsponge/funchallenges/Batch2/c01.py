# GLOBAL VARIABLES
board = [['~']*7 for j in range(6)]
gameWon = False
players = ['','']
symbols = ["X","O"]
indexCurrPlayer = 0

# SUBPROGRAMS
def printBoard():
  print('\n'*20)
  print(' 0 1 2 3 4 5 6 ')
  for row in board:
    rowString =''
    for item in row:
        rowString += (f'{item}|')
    print(f'|{rowString}') 


def placePiece(currBoard, currCol, currSymbol):
  for rowsChecked in range(len(currBoard)):
    if currBoard[5-rowsChecked][currCol] == "~":
      currBoard[5-rowsChecked][currCol] = currSymbol
      return
  raise RuntimeError('THAT IS FULL!')


def checkWon(currBoard): 
  # this long function is called to check if the game is won

  # check horizontals for a connect 4
  check = ''
  for row in currBoard:
    for square in row:
        check += square
    check += ","   

  #check verticals for a connect 4
  for pos in range(len(currBoard[0])):
    for row in currBoard:
      check += row[pos]
    check += ","

  # check diagonals for a connect 4
  for row in range(len(currBoard)):
    for column in range(len(currBoard[0])):
        
      # check / diagonal spaces for a connect 4
      for i in range(4):
        if row-i >= 0 and column+i < len(currBoard[0]):
          check += currBoard[row-i][column+i]
      check += ","

      # TASK 2 ==> check \ diagonal spaces for a connect 4 
      # copy the 4 lines of / check above to help you

  # return the result
  return symbols[0]*4 in check or symbols[1]*4 in check  

# MAIN PROGRAM
while not gameWon:
  printBoard()
  try:
    # TASK 1 the line below includes the current player in the instruction but this is currently blank
    # ==> modify a line of code towards the start of this code file to give names to the players using two inputs.
    colChosen = int(input(f'{players[indexCurrPlayer]}  select a row (0-6): '))     
    if colChosen in range(0, len(board[0])):
      placePiece(board, colChosen, symbols[indexCurrPlayer])
      gameWon = checkWon(board)
      indexCurrPlayer = (indexCurrPlayer + 1) % len(players)
    else:
      raise ValueError("invalid column number")
  except ValueError:
    input('only enter valid column numbers please ... press enter to try again...')

printBoard()
# TASK 3: ==> Currently there are no messages when the game is finished
# print the winner or a message saying it is a draw
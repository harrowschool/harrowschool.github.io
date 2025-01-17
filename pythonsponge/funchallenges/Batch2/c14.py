# Constants for Mini-Othello board size
BOARD_SIZE = 6
WHITE = "W"
BLACK = "B"

# This code initialises the board
board = [["□"] * BOARD_SIZE for _ in range(BOARD_SIZE)]
# This code sets up the starting pieces
board[2][2], board[2][3], board[3][2], board[3][3] = BLACK, WHITE, WHITE, BLACK

def printBoard(board):
  print("  " + " ".join([str(i+1) for i in range(BOARD_SIZE)]))
  for idx, row in enumerate(board):
    print(f"{idx+1} {' '.join(row)}")

def flipDiscs(board, row, col, player):
  opponent = WHITE if player == BLACK else BLACK
  directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
  flipped = 0

  for dx, dy in directions:
    discs_to_flip = []
    x, y = col + dx, row + dy
    while x in range(BOARD_SIZE) and y in range(BOARD_SIZE) and board[y][x] == opponent:
      discs_to_flip.append((y, x))
      x += dx
      y += dy

    if x not in range(BOARD_SIZE) or y not in range(BOARD_SIZE) or board[y][x] != player:
      continue
    
    for y, x in discs_to_flip:
      board[y][x] = player
    flipped += len(discs_to_flip)

  # This function returns the number of flipped discs
  return flipped

def RunGame():
  players = [WHITE, BLACK] 
  player = 0 
  scores = [2, 2]
  passCount = 0

  while True:
    printBoard(board)
    print(f"Current Scores: White={scores[0]}, Black={scores[1]}")
    print("Player " + players[player] + "'s turn")
    
    rowInp = input("Enter row (1-6) or 0 to pass: ")
    
    if rowInp == "0":
      passCount += 1
    else:
      passCount = 0   
      colInp = input("Enter column (1-6): ")
      
      # ==> TASK 1: Improve this validation 
      # (to also check that the row and column are both between 1 and 6)
      if not rowInp.isdigit() or not colInp.isdigit():
        print("Invalid input!")
        continue
      
      row = int(rowInp) - 1
      col = int(colInp) - 1

      # This code places the disc and flips outflanked discs
      board[row][col] = players[player]
      changed = flipDiscs(board, row, col, players[player])
      scores[player] += (1 + changed)
      scores[1-player] -= changed

    # ==> TASK 2: Also end the game if the total of the two scores is 36 (board is full)
    if passCount == 2:
      print("GAME OVER!")
      # ==> TASK 3: Find and declare the winner or a tie
      return

    player = 1 - player

RunGame()

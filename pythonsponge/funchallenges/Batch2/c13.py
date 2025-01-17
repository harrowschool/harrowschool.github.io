import random
import os
from itertools import product
 
grid = [[0 for _ in range(4)] for _ in range(4)]
score = 0
 
def print_grid():
    os.system("cls")
    print("2048\n")
    for row in range(4):
        print("-"*25)
        print("     ".join(["|" for _ in range(5)]))
        for col in range(4):
            print(f"|{num if (num := grid[row][col]) != 0 else '' :^5}", end='')
        print("|")
        print("     ".join(["|" for _ in range(5)]))
    print("-"*25)
    print("\nScore: ", score, "\n")
 
# TASK 2: The board is incorrectly generating 4s instead of 2s on every turn. Can you change it to generate 2s instead?
def generate_twos():
    available_sqrs = []
    for row in range(4):
        for col in range(4):
            if grid[row][col] == 0:
                available_sqrs.append((row, col))
    if not available_sqrs:
        return
    random_square = random.choice(available_sqrs)
    row, col = random_square
    grid[row][col] = 4
 
# HINT FOR TASK 3: the code should go in these 4 functions below
def merge_up():
    global grid, score
    for col in range(4):
        for curr_row in range(3):
            for next_row in range(curr_row+1, 4):
                if grid[curr_row][col] == grid[next_row][col]:
                    grid[curr_row][col] *= 2
                    grid[next_row][col] = 0
                elif grid[curr_row][col] == 0 and grid[next_row][col] != 0:
                    grid[curr_row][col] += grid[next_row][col]
                    grid[next_row][col] = 0
 
def merge_left():
    global grid, score
    for row in range(4):
        for curr_col in range(3):
            for next_col in range(curr_col+1, 4):
                if grid[row][curr_col] == grid[row][next_col]:
                    grid[row][curr_col] *= 2
                    grid[row][next_col] = 0
                elif grid[row][curr_col] == 0 and grid[row][next_col] != 0:
                    grid[row][curr_col] += grid[row][next_col]
                    grid[row][next_col] = 0
  
def merge_down():
    global grid, score
    for col in range(4):
        for curr_row in range(3, -1, -1):
            for next_row in range(curr_row -1, -1, -1):
                if grid[curr_row][col] == grid[next_row][col]:
                    grid[curr_row][col] *= 2
                    grid[next_row][col] = 0
                elif grid[curr_row][col] == 0 and grid[next_row][col] != 0:
                    grid[curr_row][col] += grid[next_row][col]
                    grid[next_row][col] = 0
 
def merge_right():
    global grid, score
    for row in range(4):
        for curr_col in range(3, -1, -1):
            for next_col in range(curr_col - 1, -1, -1):
                if grid[row][curr_col] == grid[row][next_col]:
                    grid[row][curr_col] *= 2
                    grid[row][next_col] = 0
                elif grid[row][curr_col] == 0 and grid[row][next_col] != 0:
                    grid[row][curr_col] += grid[row][next_col]
                    grid[row][next_col] = 0
 
def adjacent_cells(row, col):
    for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        nr, nc = row + dr, col + dc
        if 0 <= nr < 4 and 0 <= nc < 4:
            yield (nr, nc)
 
# TASK 5 function (HINT: check if at least one adjacent cell of any cell has the same value -> return True)
def can_merge():
    for row in range(4):
        for col in range(4):
            for nr, nc in adjacent_cells(row, col):
                pass
 
# TASK 1: The game currently ends when you get the 512 tile. Can you change it to end only when you get the 2048 tile?
def win_condition():
  return 512 in (grid[0] + grid[1] + grid[2] + grid[3])
        
while True:
 
    generate_twos()
    print_grid()
 
    # TASK 5: When the board is completely full, the game doesn't check if there are still legal moves to play and ends the game. Can you complete the can_merge() function and use it to fix this?
    if all([grid[r][c] != 0 for r, c in list(product(range(4), repeat=2))]):
        print_grid()
        print("You lost!")
        break
 
    if win_condition():
        print("You won!")
        break
    
    # TASK 4: Currently, the game doesn't quit when the user types the letter Q. Can you fix this?
    while True:
        choice = input("Type W to swipe up, S to swipe down, A to swipe left, D to swipe right, Q to quit: ").upper()
        if choice in ("Q", "W","S","A","D"):
            break
        else:
            print("Invalid input")
    if choice == "W":
        merge_up()
    elif choice == "S":
        merge_down()
    elif choice == "A":
        merge_left()
    elif choice == "D":
        merge_right()
    
    # TASK 3: The game is incorrectly giving points for every move not every merge. 
    # Can you change it to give points per every merge by adding the value of each tile you merge?
    # HINT: add the value of the tile created after every merge in merge_up(), merge_down(), merge_left() and merge_right() functions
    score += 10
 
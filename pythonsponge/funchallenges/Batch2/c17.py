#################
# LIBRARY IMPORTS
#################

from copy import deepcopy
import time

# Import key functions for pacman game
from pacmanlib import next_ghost_move
from pacmanlib import clear_screen
from pacmanlib import find_empty_spot
from pacmanlib import find_symbol_position
from pacmanlib import load_custom_map
from pacmanlib import print_coloured_text

###############
# CONSTANTS
###############

STUN_TIME = 20
NUM_FOOD = 15
NUM_SPECIAL_FOOD = 5

# Symbols used for rendering
EMPTY_SQUARE = '.'
PLAYER_SYMBOL = 'P'
GHOST_SYMBOL = "G"
STUNNED_GHOST_SYMBOL = "G"
FOOD_SYMBOL = '*'
SPECIAL_FOOD_SYMBOL = '$'
WALL_SYMBOL = '#'

'''Uncomment these lines to reveal a more interesting board appearance! (also for extension task 2)'''
# EMPTY_SQUARE = '\U00002B1C'
# PLAYER_SYMBOL = '\U0001F642'
# GHOST_SYMBOL = "\N{ghost}"
# STUNNED_GHOST_SYMBOL = "\N{headstone}"
# FOOD_SYMBOL = '\U0001F352'
# SPECIAL_FOOD_SYMBOL = '\U0001F36A'
# WALL_SYMBOL = '\U00002B1B'

# ==> TASK 1: Fix players walking through walls. The PLAYER_VALID_SQUARES tuple stores types of squares that the player can walk into.
PLAYER_VALID_SQUARES = (".", "G", "#")

###############
# SUBPROGRAMS
###############


def print_board(board, foods, special_foods, score, stun_duration):
    # Function to print the game board
    clear_screen()
    print("="*17)
    print(f"{'PACMAN GAME':^17}")
    print("="*17)
    print()
    for r, row in enumerate(board):
        for c, char in enumerate(row):
            if char == "P":
                print_coloured_text(text=PLAYER_SYMBOL,
                                    colour="yellow", end='')  # Player
            elif char == "G":
                # ==> TASK 5:  Print ghost with green colour when stunned
                if stun_duration == 0:  # If ghosts are not stunned
                    print_coloured_text(text=GHOST_SYMBOL,
                                        colour="red", end='')  # Ghost
                else:  # If ghosts are stunned
                    # Hint: Delete this line and use the print_coloured_text function (tip: look above at how the function is used)
                    print(STUNNED_GHOST_SYMBOL, end='')
            elif (r, c) in foods:
                print_coloured_text(
                    text=FOOD_SYMBOL, colour="cyan", end='')  # Food
            elif (r, c) in special_foods:
                print_coloured_text(text=SPECIAL_FOOD_SYMBOL,
                                    colour="magenta", end='')  # Special Food
            elif char == "#":  # Wall
                print_coloured_text(
                    text=WALL_SYMBOL, colour="blue", end='')  # Wall
            elif char == ".":  # Empty space
                print(EMPTY_SQUARE, end='')
        print()
    print(f"\nScore: {score}")
    if stun_duration > 0:
        print(f"Ghosts are stunned for more {stun_duration} move(s)")


def move(direction, x, y, board, rows, cols):
    # Function to handle player movement
    if direction == 'w' and x > 0 and board[x - 1][y] in PLAYER_VALID_SQUARES:
        board[x][y] = "."
        return x - 1, y
    elif direction == 's' and x < rows - 1 and board[x + 1][y] in PLAYER_VALID_SQUARES:
        board[x][y] = "."
        return x + 1, y
    elif direction == 'a' and y > 0 and board[x][y - 1] in PLAYER_VALID_SQUARES:
        board[x][y] = "."
        return x, y - 1
    elif direction == 'd' and y < cols - 1 and board[x][y + 1] in PLAYER_VALID_SQUARES:
        board[x][y] = "."
        return x, y + 1
    return x, y


def move_ghosts_towards_player(ghosts, board, pacman_x, pacman_y):
    # Move ghosts towards the player
    for ghost in ghosts:
        next_move = next_ghost_move(
            (ghost[0], ghost[1]), (pacman_x, pacman_y), board)
        if next_move is not None:  # Check if ghost has a square to move to
            board[ghost[0]][ghost[1]] = "."  # Clear old position
            ghost[0], ghost[1] = next_move
            board[ghost[0]][ghost[1]] = "G"  # Set new position


def check_collision(pacman_x, pacman_y, ghosts, foods, score, special_foods, stun_duration):
    # Check for collisions between player, ghosts, and food
    if stun_duration == 0:  # Check if stun duration is 0 (ghosts free to move)
        if [pacman_x, pacman_y] in ghosts:
            return
    else:  # Ghosts can be eaten
        # ==> TASK 3: Player does not get score for eating a ghost.
        if [pacman_x, pacman_y] in ghosts:  # Check if player collides with ghost
            ghosts.remove([pacman_x, pacman_y])
            for x, y in GHOST_RESPAWN_POINTS:
                if [x, y] not in ghosts:
                    ghosts.append([x, y])
                    break
    if (pacman_x, pacman_y) in foods:
        score += 1
        foods.remove((pacman_x, pacman_y))
    if (pacman_x, pacman_y) in special_foods:
        score += 2
        # Remove the special food from the set
        special_foods.remove((pacman_x, pacman_y))
        stun_duration = STUN_TIME
    return score, stun_duration

###############
# MAIN PROGRAM
###############


# Create the board
board = load_custom_map()
rows, cols = len(board), len(board[0])

# Get coordinates of player
pacman_x, pacman_y = find_symbol_position(board, 'P', rows, cols)

# Get coordinates of ghosts
ghosts = [[row, col]
          for row in range(rows) for col in range(cols) if board[row][col] == 'G']

# Normal food configuration
foods = set()
for _ in range(NUM_FOOD):
    food_x, food_y = find_empty_spot(board, rows, cols)
    foods.add((food_x, food_y))

# Special food configuration
special_foods = set()
for _ in range(NUM_SPECIAL_FOOD - 1):
    food_x, food_y = find_empty_spot(board, rows, cols)
    special_foods.add((food_x, food_y))
special_foods.add((5, 2))

GHOST_RESPAWN_POINTS = deepcopy(ghosts)  # Get ghost respawn points
stun_duration = 0  # Stun duration in moves
score = 0  # Initial score

# Main game loop
while True:

    try:
        # Display the game board
        print_board(board, foods, special_foods, score, stun_duration)

        # Check if player ate all the food and special food
        if len(foods) == 0 and len(special_foods) == 0:
            print("You won the game!")
            break

        # ==> TASK 2:  Print an error message if the user does not type w, a, s or d. The ghosts should not move until the player enters a valid command.
        key = input("Enter a move (w/a/s/d): ").lower()
        pacman_x, pacman_y = move(
            key, pacman_x, pacman_y, board, rows, cols)  # Move pacman

        # ==> TASK 4: Add an if statement to check if stun duration is greater than 0 to prevent it from going negative
        stun_duration -= 1  # Decrement stun duration

        board[pacman_x][pacman_y] = "P"  # Update board

        if stun_duration == 0:
            # Move ghosts towards player if ghosts are not stunned
            move_ghosts_towards_player(ghosts, board, pacman_x, pacman_y)

        game_output = check_collision(pacman_x, pacman_y, ghosts,
                                      foods, score, special_foods,
                                      stun_duration)  # Check collisions between player and objects
        if game_output is None:
            raise IndexError
        else:
            score, stun_duration = game_output
        time.sleep(0.1)

    except IndexError:
        print("Game Over! Your score: {}".format(score))
        break

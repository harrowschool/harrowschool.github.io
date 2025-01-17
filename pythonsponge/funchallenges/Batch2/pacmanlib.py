'''LIBRARY FILES TO IMPORT'''

import random
import os

# Colours dictionary
COLOURS = {'black': 30, 'red': 31, 'green': 32, 'yellow': 33,
           'blue': 34, 'magenta': 35, 'cyan': 36, 'white': 37}


def a_star(start, goal, board):
    # A* algorithm for pathfinding
    open_set = [start]
    came_from = {}
    g_score = {start: 0}

    while open_set:
        current = min(open_set, key=lambda x: g_score[x] + heuristic(x, goal))

        if current == goal:
            path = reconstruct_path(came_from, start, goal)
            return path

        open_set.remove(current)

        for neighbor in neighbors(current):
            if board[neighbor[0]][neighbor[1]] in '#G':
                continue  # Skip walls

            tentative_g_score = g_score[current] + 1

            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score

                if neighbor not in open_set:
                    open_set.append(neighbor)

    return []


def heuristic(a, b):
    # Heuristic function for A*
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def neighbors(node):
    # Function to get neighboring nodes
    x, y = node
    return [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]


def reconstruct_path(came_from, start, goal):
    # Reconstruct path from A* algorithm
    current = goal
    path = [current]
    while current != start:
        current = came_from[current]
        path.append(current)
    return path[::-1]


def next_ghost_move(ghost_coord, pacman_coord, board):
    # Function to get next ghost move using A* pathfinding algorithm
    path = a_star(ghost_coord, pacman_coord, board)
    if path:
        return path[1]


def clear_screen():
    # Function to clear the console screen
    os.system('cls' if os.name == 'nt' else 'clear')


def find_empty_spot(board, rows, cols):
    # Find an empty spot on the board
    empty_spots = [(row, col) for row in range(rows)
                   for col in range(cols) if board[row][col] == '.']

    if not empty_spots:
        return None, None

    return random.choice(empty_spots)


def find_symbol_position(board, symbol, rows, cols):
    # Find the position of a symbol on the board
    for row in range(rows):
        for col in range(cols):
            if board[row][col] == symbol:
                return row, col
    return None, None


def load_custom_map():
    # Function to load custom map from map.txt
    with open('map.txt', 'r') as f:
        custom_map = [i for i in f.read().splitlines()]
    return [list(row) for row in custom_map]


def print_coloured_text(text, colour, end):
    # Function to print coloured text using ANSI terminal codes
    print(f'\033[{COLOURS[colour]};1;1m{text}\033[0m', end=end)

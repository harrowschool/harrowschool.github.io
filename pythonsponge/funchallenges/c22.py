# CHESS PIECES
# Run the program to see how some chess pieces move to nearby squares
# Then complete the tasks to extend the functionality

# DON'T CHANGE THIS LINE
____ = ""


# THIS DICTIONARY MAPS CHESS PIECE NAMES TO A LIST OF LEGIT MOVES WITHIN A SURROUNDING 5x5 GRID
movesets = {
    "ROOK": [(0, 2), (1, 2), (3, 2), (4, 2), (2, 0), (2, 1), (2, 3), (2, 4)],
    "BISHOP": [(0, 0), (1, 1), (3, 3), (4, 4), (0, 4), (1, 3), (3, 1), (4, 0)],
    "KNIGHT": [(0, 1), (0, 3), (1, 0), (1, 4), (3, 0), (3, 4), (4, 1), (4, 3)],
    # TASK 1: Add moves for the KING. It should have the following moves:
    # [(1, 1), (1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2), (3, 3)]
    # TASK 2: Research and add moves for the QUEEN also
}

for name, moves in movesets.items():
    print(name)
    for y in range(5):
        for x in range(5):
            if (x, y) == (2, 2):
                # TASK 3: Instead of a #, use the FIRST LETTER of the piece name
                # hint: the piece name is stored in the `name` variable. Use string indexing to get the first letter
                print("#", end="")
            elif (x, y) in moves:
                print("x", end="")
            else:
                print(".", end="")
        print()
    print()

# TASK 4: Complete the blanks to print out the pawn values of each piece and add the QUEEN also
piece_values = {"ROOK": 5, "BISHOP": 3, "KNIGHT": 3}
print("PIECE VALUES:")
for name, value in piece_values.items():
    print(f"A {____} IS WORTH {____} PAWNS")


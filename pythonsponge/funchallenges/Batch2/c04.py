# TASK 1: Replace the ? below with a letter to complete the crossword
# The word you make should be related to programming. It's a word used elsewhere in this code.
grid = """
COMPUTER IP
O E N  S D 
DOMAINNAME 
E O O A   E
  R NEUMANN
JOY   R   C
A    N  F?R
VIDEOGAME Y
A A  R  I P
  T  APPLET
ADA  M  D  
"""[1:-1].split("\n")

# Just used for leaving gaps in the code
___ = "_"

words = []
word = ""

# Go through the grid row by row
for row in range(len(grid)):
    # Go through each row, column by column
    for col in range(len(grid[0])):
        letter = grid[row][col]
        # As we find consecutive letters, build up a word
        if letter != " ":
            word += letter
        # When we find a space, print the word and reset
        elif word != "":
            # TASK 2: Currently, the program finds a "word" even when there's only one letter in a row
            # Put the `print` below inside an `if` statement so we only print if there's more than one letter
            # Do the same with the other print statement below
            print(word)
            words.append(word)
            word = ""
    # We also print and reset when we reach the edge of the grid
    if word != "":
        print(word)
        words.append(word)
        word = ""

# TASK 3: Allow the program to find vertical words
# We can use the same code from above (from the first `word = ""` to here) with one small change so that we go column
# by column first rather than row by row first.
# Copy the code from above and change one or two lines to swap rows with columns

# TASK 4: Find the longest word in the crossword
# To find the longest word, we look at each word in turn, remembering the longest word found so far and updating if we
# find a longer one. Implement this algorithm below by filling in the blanks.

longest_so_far = ""
for i in range(len(words)):
    # Get the item at position `i` in the list `words`
    current_word = ___
    # Find and compare the lengths of the two words
    if ___ > ___:
        # Update our longest found word
        ____ = current_word

if longest_so_far != "":
    # Print the result
    print(f"The longest word found was {___} of length {len(___)}")

# TASK 5: Allow the user to input a letter e.g. N
# Then find and output the location of every occurence of that letter in the crossword
# You will need to iterate through each row and column, just as the code which finds all the words does
# Then you will need an `if` statement to check if the letter at each location is the requested letter
# ... and if so, print the coordinate in terms of its column and row numbers

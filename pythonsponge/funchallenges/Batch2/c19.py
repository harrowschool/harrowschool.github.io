##############
# LIBRARIES
##############

import random
from random import shuffle
import time

##############
# Colour codes for the foreground and background along with some useful text emphasis codes
##############


class fg:
    black = "\u001b[30m"
    red = "\u001b[31m"
    green = "\u001b[32m"
    yellow = "\u001b[33m"
    blue = "\u001b[34m"
    magenta = "\u001b[35m"
    cyan = "\u001b[36m"
    white = "\u001b[37m"
    def rgb(r, g, b): return f"\u001b[38;2;{r};{g};{b}m"


class bg:
    black = "\u001b[40m"
    red = "\u001b[41m"
    green = "\u001b[42m"
    yellow = "\u001b[43m"
    blue = "\u001b[44m"
    magenta = "\u001b[45m"
    cyan = "\u001b[46m"
    white = "\u001b[47m"
    def rgb(r, g, b): return f"\u001b[48;2;{r};{g};{b}m"


class util:
    reset = "\u001b[0m"
    bold_on = "\u001b[1m"
    bold_off = "\u001b[21m"
    underline_on = "\u001b[4m"
    underline_off = "\u001b[24m"
    reverse = "\u001b[7m"
    clear = "\u001b[2J"

##############
# SUBPROGRAMS
##############


def get_word_list():
    file = open("wordsearchwords.txt", "r")
    words = file.read().split(", ")
    shuffle(words)
    return words[:6]


def generate_word_search(words, size=10):
    # Create an empty grid
    grid = [[' ' for _ in range(size)] for _ in range(size)]
    wordDict = {}

    # Place words horizontally or vertically
    for word in words:
        originalWord = word
        placed = False
        while not placed:

            direction = random.choice(['horizontal', 'vertical'])

            if random.randint(0, 1) == 0:  # reverse word half of the time
                word = word[::-1]

            if direction == 'horizontal':
                row = random.randint(0, size - 1)
                col = random.randint(0, size - len(word))
                wordPos = []
                if all(grid[row][col + i] == ' ' or grid[row][col + i] == word[i] for i in range(len(word))):
                    for i in range(len(word)):
                        grid[row][col + i] = word[i]
                        wordPos.append((row, col + i))
                    placed = True
                    wordDict[originalWord] = wordPos

            else:  # vertical
                row = random.randint(0, size - len(word))
                col = random.randint(0, size - 1)
                wordPos = []
                if all(grid[row + i][col] == ' ' or grid[row + i][col] == word[i] for i in range(len(word))):
                    for i in range(len(word)):
                        grid[row + i][col] = word[i]
                        wordPos.append((row + i, col))
                    placed = True
                    wordDict[originalWord] = wordPos

    # Fill the remaining spaces with random letters
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in range(size):
        for j in range(size):
            if grid[i][j] == ' ':
                grid[i][j] = random.choice(letters)

    return grid, wordDict


def display_word_search(grid, positions):

    # red line
    print(bg.red + " " * len(grid) * 2 + bg.white)

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if (row, col) in positions:
                print(fg.green + util.bold_on +
                      grid[row][col] + util.bold_off + " ", end="")
            else:
                print(fg.black + grid[row][col] + " ", end="")
        print("\n", end="")

    # red line
    print(bg.red + " " * len(grid) * 2)

    # reset the colours for the instructions and prompt
    print(util.reset + "")


def play_word_search(words, size=10):

    grid, wordDict = generate_word_search(words, size)
    foundPositions = set()
    display_word_search(grid, foundPositions)

    print(
        f"Find the computer-science related words! There are {len(words)} words to find and they are all at least 4 letters long.")
    print("Words can be horizontal or vertical, and can be reversed. For example, 'PYTHON' might be in the puzzle as 'NOHTYP'.")

    count = len(words)
    foundWords = set()

    startTime = time.time()

    while count > 0:
        # ==> TASK 1: On the line below, display how many words remain to be found (this value is stored in the variable called count). For example, if there are 3 words remaining, the output could be "There are 3 words remaining."

        found = False
        while not found:
            guess = input(
                "Enter your guess (or 'exit' to stop and have the answer displayed): ").upper()

            if guess == 'EXIT':
                print("The word search solution was:")
                foundPositions = set()
                print("The words were: ", end="")
                print((", ".join(words)))
                for word in words:
                    foundPositions |= set(wordDict[word])
                print()
                display_word_search(grid, foundPositions)
                return

            if guess in words and guess not in foundWords:
                print(f"Found {guess}!")
                foundPositions |= set(wordDict[guess])
                display_word_search(grid, foundPositions)
                found = True
                foundWords.add(guess)

            # ==> TASK 2: On the line below, add an elif statement so that if the user tries to guess a word that has already been found, a message is displayed to tell them that they have already found that word.

            else:
                print("Incorrect. Try again.")
        count -= 1

    endTime = time.time()
    timeDif = endTime - startTime

    # ==> TASK 3: Edit the two lines below so that the values of minutes and seconds is correct (timeDif is the total time the user has taken in seconds). For example, 80 seconds should be displayed as "1 minute and 20 seconds".
    minutes = 0
    seconds = 0
    print(
        f"Congratulations! You found all the words. It took you {minutes} minute and {seconds} seconds.")

##############
# MAIN PROGRAM
##############


# ==> TASK 4: Can you put the two lines below into a while loop that will keep the game running until the user enters 'quit'?
word_list = get_word_list()
play_word_search(word_list)

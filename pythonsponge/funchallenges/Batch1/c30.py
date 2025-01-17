# ANAGRAMS
from random import choice, shuffle
from time import time

# SCROLL DOWN TO FIND THE PUZZLE TASKS

WORD_LENGTH = 5
# 15 seconds to guess the anagram
GAME_TIME = 15 

# This encodes the words in ASCII with the newline char (ASCII 10) as a separator
encodedW = [
  97,99,116,111,114,10,97,99,116,10,116,97,99,10,116,97,114,10,114,97,116,
  10,114,111,116,97,10,99,97,114,116,10,99,97,114,10,111,114,99,97,10,112,
  111,115,116,115,10,115,116,111,112,115,10,115,112,111,116,115,10,116,111,
  112,115,10,115,112,111,116,10,115,116,111,112,10,112,111,115,116,10,112,
  111,116,115,10,111,112,116,115,10,111,112,116,10,112,111,116,10,116,111,
  112,10,115,111,112,10,109,105,108,101,115,10,115,109,105,108,101,10,108,
  105,109,101,115,10,108,105,109,101,10,109,105,108,101,10,115,108,105,109,
  101,10,115,105,108,101,10,108,105,109,115,10,115,108,105,109,10,108,105,
  109,10,109,105,108,10,115,105,109,10,111,117,103,104,116,10,103,117,116,
  10,116,117,103,10,104,117,103,10,104,117,116,10,116,111,117,103,104,10,
  103,111,116,10,111,117,116,10,104,111,116,10,104,111,103,10,115,116,101,
  97,107,10,116,97,107,101,115,10,115,107,97,116,101,10,115,116,97,107,101,
  10,116,97,107,101,10,116,97,115,107,10,101,97,116,115,10,101,97,115,116,
  10,116,101,97,115,10,116,101,97,10,115,101,97,116,10,115,97,116,10,115,
  101,116,10,115,97,107,101,10,116,97,115,101,10,116,111,115,115,10,97,112,
  112,108,121,10,108,97,112,10,112,97,108,10,108,97,121,10,112,97,121,10,
  97,112,112,10,121,97,112,10,112,108,121,10,115,105,122,101,100,10,115,
  105,122,101,10,122,101,100,10,115,105,100,101,10,100,105,101,10,100,105,
  101,115,10,109,111,117,115,101,10,115,117,109,111,10,115,111,109,101,10,
  117,115,101,10,109,117,115,101,10,115,117,101,10,101,109,117,10,101,109,
  117,115,10,115,101,109,105,10,101,108,109,115,10,101,108,109,10,100,105,
  115,10,108,97,112,112,121,10,112,97,108,112,10,112,108,97,121,10,105,110,
  102,101,114,10,102,105,114,101,10,102,105,110,101,114,10,102,105,110,101,
  10,102,101,114,110,10,114,101,105,110,10,102,105,110,10,102,101,110,10,
  102,105,114,10,114,105,102,101,10,116,104,111,117]

# This gets the list of English words from above - you don't need to understand this
wList = "".join([chr(c) for c in encodedW]).split("\n")

wordSet = set()
wordChoices = list()

for w in wList:
  if 2 < len(w) < WORD_LENGTH + 1:
    lW = w.lower()
    wordSet.add(lW)
    if len(w) == WORD_LENGTH:
      wordChoices.append(lW)

wordChoice = choice(wordChoices)
startTime = time()

lettersList = list(wordChoice)
# TASK 1 ==> we need to print out the player's letters scrambled so add some code to shuffle the letters
# (add a line below which uses the random shuffle function to shuffle the list)

letters = " ".join(lettersList)
score = 0

def timeUp(timeDelta):
    if timeDelta>=GAME_TIME:
        print("Time is up!")
        return True
    return False

print("find the full word or any shorter words using these letters...")
print("Enter 'q' to quit / give up: ")

while True:

    deltaTime = time() - startTime
    print(f"Letters: {letters}")
    print(f"Time left: {max(GAME_TIME-deltaTime,0):.2f}")
    print(f"Current score: {score}")
    if timeUp(deltaTime):
        break # The timer ran out
    
    # Here we input a guess
    wordGuess = input()
    if wordGuess == "q": break
    
    # First we check that all letters are valid and not used too many times
    lettersUsed = lettersList.copy() # Here we make a copy of the letters
    invalidGuess = False
    
    for l in wordGuess:
        if l in lettersUsed:
            lettersUsed[lettersUsed.index(l)] = "" # Remove the letter from the list
        else:
            # If it isn't in the list, the letter isn't valid
            invalidGuess = True
            break
    
    # If the guess is invalid, don't check if it is a real word
    if invalidGuess: continue
    # The guess is valid so we check if it is a real word
    
    if wordGuess in wordSet:
        # We calculate the points for the word
        # TASK 2 => can you change this so that the score is doubled if it is a full length word?
        # (is there already a variable storing the full word length in the code?)
        score += 100 * len(wordGuess)
        # TASK 3 => stop the user from guessing this word again
        # (we do not need any new variables or lists to do this)
    
    print()

print(f"Your score was: {score}")
print(f"The full word was {wordChoice}")
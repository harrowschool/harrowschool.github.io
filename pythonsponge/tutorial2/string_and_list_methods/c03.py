import random

colours = ['red', 'green', 'blue', 'yellow', 'orange', 'purple', 'brown']

choice = random.choice(colours)

letters = input("Guess the first two letters of my colour: ").lower()

# .startswith() ireturns True if the string starts with the specified characters
if choice.startswith(letters):
    print(f"You guessed correctly, it was {choice}")
else:
    print(f"Sorry, it was {choice}")


import random

options = ["rock", "paper", "scissors"]


computer = ___.___(___)
player = input("Choose rock, paper, or scissors: ").lower()

print("Computer chose", computer)
print(("Tie", "You win", "You lose")[(options.index(player) - options.index(computer)) % 3])

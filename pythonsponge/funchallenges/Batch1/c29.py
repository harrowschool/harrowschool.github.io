# Top trumps
import random

# The top of the deck is the start of the list
cards = [
    [0, 6, 9, 4], [3, 8, 6, 1], [1, 5, 1, 6], [9, 2, 0, 0], [7, 3, 2, 9],
    [8, 1, 4, 7], [6, 4, 5, 2], [5, 0, 7, 3], [2, 9, 3, 8], [4, 7, 8, 5]
]
random.shuffle(cards)

# TASK 1 ==> change the line below so that player 0 gets half of the cards and player 1 gets the rest
decks = [cards[:4], cards[4:]]

print("Starting decks:")
print(f"Player 0: {decks[0]}")
print(f"Player 1: {decks[1]}")

choice = input("Enter y for step mode (pause each turn) or n to play the whole game: ").lower()

current_player = 0
while len(decks[0]) > 0 and len(decks[1]) > 0:
    print(f"Player {current_player}'s turn")

    current_card = decks[current_player].pop(0)
    opponent_card = decks[1 - current_player].pop(0)
    print(f"Cards: {current_card} and {opponent_card}")

    # TASK 2 ==> Change the code below to choose the largest score on the current card
    strength = random.choice(current_card)

    # TASK 3 ==> Add the line `current_player = 1 - current_player` somewhere below (be careful, not too early) to swap the turn over. 
    opponent_strength = opponent_card[current_card.index(strength)]
	
    # TASK 4 ==> Rather than printing out the number of the category, print a category name of your choice based on the number e.g. speed/strength
    print(f"Category {current_card.index(strength) + 1} is chosen")

	# TASK 5: ==> Change the code below to append `current_card` then `opponent_card` if `current_card` is better, or `opponent_card` then `current_card` otherwise
	
    # Current player wins this card
    if strength > opponent_strength:        
        decks[current_player].append(current_card)
        decks[current_player].append(opponent_card)   
    # Opponent wins this card
    else:
        decks[1 - current_player].append(current_card)
        decks[1 - current_player].append(opponent_card)

    if choice == "y":
      choice = "" if input("press enter to continue or r to run to end: ").lower() == "r" else choice

if len(decks[0]) > 0:
    print("Player 0 wins!")
else:
    print("Player 1 wins!")
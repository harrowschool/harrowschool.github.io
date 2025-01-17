NUM_ITEMS = 10
# TASK 1 ==> Replace this constant with looking up a nice unicode character to represent the back of a card
CARDBACK = "#"

available_cards = [
    "apple", "pear", "apple", "grape", "grape","banana", "sprite", "pear", "banana", "sprite"
]

mask_list = []

for i in range(NUM_ITEMS):
    mask_list.append(CARDBACK)

print("Welcome to the matching cards game! The first card is at position 0 and the last is at position 9.")

# TASK 2 ==> Change the while loop condition so this ends when all the pairs have been found
while True:
    print(mask_list)

    guess1 = int(input("Enter a number between 0 and 9: "))
    item1 = available_cards[guess1]
    print("you've found a: " + item1)

    guess2 = int(input("Enter another number between 0 and 9: "))
    item2 = available_cards[guess2]
    print("...and now a: " + item2)

    if item1 == item2:
        print("You found a match!")
        mask_list[guess1] = item1
        mask_list[guess2] = item1

    
    else:
        print("Sorry, try again.")

# TASK 3 ==> Can you fix this error?
print(Congratulations)

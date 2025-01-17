import random

DIRECTIONS = ("left", "right")
EVENTS = ["dead end", "monster", "trap"]
CORRECT_ROUTE = ["left", "right", "left"]

current_path = []
escaped = False

print("You cautiously follow a road into the forest...\n")

while not escaped:

    direction = input("right or left or quit? ").lower()

    if direction == "quit":
	    break
    elif direction == CORRECT_ROUTE[len(current_path)]:
        print("...all seems quiet...you keep walking...")
        current_path.append(direction)
    else:
        print("Oh no! You've reached a " + random.choice(EVENTS))
        print("...you run in a panic, but now you're right back where you first started; run the program to try again!")
        break
import random

randomNumber = random.randint(1, 5)

print("The randomly generated number was", randomNumber)

if randomNumber < 3:
    print("That's a small number")
else:
    print("That's a pretty big number")

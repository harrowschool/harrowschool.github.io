from itertools import product
import random


def getRandomLocationForShip(coords, shipLength, takenCoords):
    coordsCopy = coords.copy()
    for c in takenCoords:
        dirs = product([0, 1, -1], [0, 1, -1])
        for d in dirs:
            newCo = (c[0]+d[0], c[1]+d[1])
            if newCo in coordsCopy:
                coordsCopy.remove(newCo)
    while True:
        horizontal = True if random.randint(0, 1) == 0 else False
        randomCo = random.choice(coordsCopy)
        valid = True
        finalPositions = []
        for s in range(shipLength):
            if horizontal:
                newCo = (randomCo[0]+s, randomCo[1])
            else:
                newCo = (randomCo[0], randomCo[1]+s)
            if newCo not in coordsCopy:
                valid = False
                break
            else:
                finalPositions.append(newCo)
        if valid:
            return finalPositions


def displayGrid(dim, shipLoc, missedLoc):
    shipCo = {}
    for key in shipLoc:
        for co in shipLoc[key]:
            shipCo[co] = key
    print("  ", end="")
    for i in range(dim):
        print(i, end=" ")
    print()
    for i in range(dim):
        print(i, end=" ")
        for j in range(dim):
            if (i, j) in shipCo:
                print(shipCo[(i, j)], end=" ")
            elif (i, j) in missedLoc:
                print("-", end=" ")
            else:
                print(" ", end=" ")
        print()
    print()


def displayGameInfo(shipStatus, ships):
    print()
    print("Your enemy has:")
    for key in shipStatus:
        message = f"- 1 {ships[key][0]} (length {ships[key][1]})"
        if shipStatus[key]:
            # Challenge 3 --> Fix the line below so that the word '(sunk)' is added to the end of the message
            message += ""
        print(message)
    print()


def hasGameEnded(shipStatus):
    for key in shipStatus:
        if not shipStatus[key]:
            return False
    return True


def getRowOrCOl(dim, isRow):
    while True:
        try:
            if isRow:
                num = int(input("Please enter the row of your next shot:> "))
            elif not isRow:
                num = int(input("Please enter the column of your next shot:> "))
        except ValueError:
            print("Please enter a single integer.")
            continue
        # Challenge 2 --> Fix the line below so that 'num' must also be greater than or equal to 0.
        if num < dim:
            return num
        else:
            print("That is not a valid row/column. Please try again.")


ships = {"A": ["aircraft carrier", 5], "B": ["battleship", 4], "S": [
    "submarine", 3], "D": ["destroyer", 3], "P": ["patrol boat", 2]}

DIM = 8
gridCoords = []
for i in range(DIM):
    for j in range(DIM):
        gridCoords.append((i, j))

shipLocations = {}
letters = ships.keys()
usedLocations = []
for l in letters:
    loc = getRandomLocationForShip(gridCoords, ships[l][1], usedLocations)
    for co in loc:
        if co not in usedLocations:
            usedLocations.append(co)
    shipLocations[l] = loc

knownLocations = {}
missedLocations = set()
shipStatus = {}
for l in letters:
    shipStatus[l] = False
shotCoords = set()

# Main program
print("Welcome to battleships!!!")
print("In this game, you have to work out the position of your enemy's ships and sink them in as few goes as possible.")

shots = 0
while not hasGameEnded(shipStatus):
    displayGameInfo(shipStatus, ships)
    displayGrid(DIM, knownLocations, missedLocations)
    print("You have taken", shots, "shots so far.")
    while True:
        row = getRowOrCOl(DIM, True)
        col = getRowOrCOl(DIM, False)
        co = (row, col)
        # Challenge 4 --> Can you first check to see if co is in shotCoords? If it is, then print a message saying that the shot has already been taken.
        # The rest of the code in the While True loop should only run if the shot has not already been taken.
        missed = True
        shotCoords.add(co)
        for key in shipLocations:
            coords = shipLocations[key]
            if co in coords:
                print()
                print("Hit!")
                missed = False
                if key in knownLocations:
                    knownLocations[key].append(co)
                else:
                    knownLocations[key] = [co]
                shipLocations[key].remove(co)
                if len(shipLocations[key]) == 0:
                    print("You have sunk the enemy's", ships[key][0]+"!")
                    shipStatus[key] = True
                break
        if missed:
            print()
            print("Miss!")
            missedLocations.add(co)
        shots += 1
        break

message = f"Congratulations! You sunk all of the enemy's ships in {shots} shots! Can you beat this?"
message = f"| {message} |"
print()
print("~"*len(message))
print(message)
# Challenge 1 --> Fix the line below so that the symbol '~' is printed as many times as the length of the message.
print("~")
print()

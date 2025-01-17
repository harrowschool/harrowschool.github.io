myPets = ["goldfish", "gerbil", "frog", "mouse"]
while True:
    guess = input("guess one of my pets: ").lower()
    if guess in myPets:
        break
    print("sorry, try again...")
print("well done!")    

import os

class Gamestate:
    def __init__(self):
        self.lifepoints = 3
        self.bag = []

class Item:
    def __init__(self):
        self.name = ""
        self.descr = ""
        self.verbs = {"examine":self.examine}
        self.currentLocation = None

    def examine(self):
      print(self.descr)

class Cheese(Item):
    def __init__(self):
        super().__init__()
        self.name = "cheese"
        self.descr = "A piece of cheese, it looks delicious!"
        self.verbs["eat"] = self.eat

    def eat(self):
        print("You eat the cheese and it tasted so good that it gave you an extra lifepoint!")
        MAINSTATE.lifepoints += 1
        print(f"You now have {MAINSTATE.lifepoints} lifepoints!")
        MAINSTATE.bag.remove(self.name)

class Torch(Item):
    def __init__(self):
        super().__init__()        
        self.name = "torch"
        self.descr = "A torch, it looks like it could be useful somewhere!"
        self.lit = False
        self.verbs["use"] = self.use

    def use(self):
        print("You light the torch and it illuminates the area around you!")
        print("You can now see where you are going in dark places!")
        if self.currentLocation.name == "tunnel":
            self.currentLocation.dirs["e"] = "win"
            self.currentLocation.extraDetail = "...with your torch lit you can just make out a passageway to the East!"
        self.lit = True

class Location:

    def __init__(self):
        self.name = "undefined"
        self.noun = None
        self.verb = None
        self.descr = ""
        self.extraDetail = ""
        self.dirs = {}
        self.contents = {}

    def arrive(self):
        while True:
            self.describe()
            if self.extraDetail != "":
                print(self.extraDetail)
            self.getinput()
            if self.verb == "go":
                if self.noun in self.dirs:
                    return WORLD[self.dirs[self.noun]]
                else:
                    print("unknown location")
            elif self.noun in self.contents or self.noun in MAINSTATE.bag:
                self.command()
            else:
                print("hmm, I don't understand that...")

    def describe(self):
        print("Current location: ", self.name)
        print(self.descr)
        print("you are carrying:", ",".join(MAINSTATE.bag))
        for item in self.contents:
            print(self.contents[item])
        print("you can go:", ",".join(list(self.dirs.keys())))

    def getinput(self):
        while True:
            action = input("> ")
            if len(action.split()) == 2:
                verb, noun = action.split()
                self.verb, self.noun = verb.lower(), noun.lower()
                os.system('cls' if os.name == 'nt' else 'clear')
                break
            else:
                print("enter two words in verb noun format...")     
    
    def command(self):
        if self.verb == "take":
            if self.noun in MAINSTATE.bag:
                print("you already have that!")
            elif self.noun in self.contents:
                MAINSTATE.bag.append(self.noun)
                print("you take the", self.noun)
                del self.contents[self.noun]
            else:
                print("you can't take that!")
        elif ITEMS[self.noun] and self.verb in ITEMS[self.noun].verbs:
            if self.noun in MAINSTATE.bag:
                ITEMS[self.noun].currentLocation = self
                ITEMS[self.noun].verbs[self.verb]()
            else:
                print("you don't have that currently!")
        else:
            print("you can't do that!")

class Tunnel(Location):
    def __init__(self):
        super().__init__()        
        self.name = "tunnel"
        self.descr = "you are in a dark tunnel"
        self.dirs = {"n": "castle", "s": "mansion"}

    def arrive(self):
        if "torch" in MAINSTATE.bag and ITEMS["torch"].lit:
            self.extraDetail = "...with your torch lit you can just make our a passageway to the East!"
            self.dirs["e"] = "win"
        else:
            self.extraDetail = "...it really is very dark in here!"
            self.dirs.pop("e", None)
        return super().arrive()

class Castle(Location):
    def __init__(self):
        super().__init__()        
        self.name = "Castle"
        self.descr = "A majestic castle, with a big gate arises in front of you!"
        self.dirs = {"s": "tunnel"}
        self.contents = {"torch": "An old rusty torch lies on the ground!"}       

class Mansion(Location):
    def __init__(self):
        super().__init__()
        self.name = "The Old Mansion"
        self.descr = "This mansion is old and spooky. It definitely has seen better days!"
        self.dirs = {"n": "tunnel", "s": "lose"}

class Lose(Location):
    def __init__(self):
        self.name = "Mansion Gardens"
        self.descr = "These gardens look very unkempt; it seems like no one has been here for a long time!"
        self.dirs = {"n": "mansion"}

    def arrive(self):
        print("A LION SPRINGS FROM THE BUSHES AND ATTACKS YOU!")
        if MAINSTATE.lifepoints > 1:
            MAINSTATE.lifepoints -= 1
            print("You have been mauled but you escape back North and still have", MAINSTATE.lifepoints, "lifepoints left!")
            return WORLD[self.dirs["n"]]
        else:
            print("Bad luck, you are out of lifepoints, you have been killed by the lion!")
            return None
        
class Win(Location):
    def __init__(self):
        self.name = "Paradise"
        self.descr = "You have escaped and won the game!"

    def arrive(self):
        print(self.descr)
        return None     

WORLD = {
    "tunnel": Tunnel(),
    "castle": Castle(),
    "mansion": Mansion(),
    "lose": Lose(),
    "win": Win()
}

ITEMS = {
    "cheese": Cheese(),
    "torch": Torch()
}

MAINSTATE = Gamestate()
MAINSTATE.bag.append("cheese")

print("WELCOME TRAVELLER TO A WORLD OF ADVENTURE! TRY TO ESCAPE THE WORLD ALIVE!")
print("ENTER TWO-WORD COMMANDS E.G. GO N, EAT PEPPER, USE STICK, TAKE STRING, EXAMINE FORK")
currentLocation = Mansion()

while currentLocation:
    currentLocation = currentLocation.arrive()

print("GAME OVER!")

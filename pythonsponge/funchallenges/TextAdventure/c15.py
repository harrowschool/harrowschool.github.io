import random

monsters = ["Ghost", "Ogre", "Goblin"]
monsterHealth = [15, 100, 50]
monsterAttack = [1, 30, 10]
playerHP = 100

def fight(monsterName):
  global playerHP
  monsterHP = monsterHealth[monsters.index(monsterName)]
  monsterDmg = monsterAttack[monsters.index(monsterName)]
  print(f"You come across a {monsterName} with {monsterHP} health. Fight!")
  while playerHP > 0 and monsterHP > ___:
    print(f"You hit the {monsterName} for 20 damage")
    monsterHP -= 20
    print(f"The {monsterName} hits you for {monsterDmg} damage")
    playerHP -=  monsterDmg

  if monsterHP <= 0:
    print(f"You survived with {________} health remaining.")
    return True # player survived
  if playerHP <= 0:
    return _____ # player died
  

def locationA():
  alive = True
  monsterChance = random.randint(1,2)
  if monsterChance == 2: # 50% chance
    monster = random.choice(monsters)
    alive = fight(monster)
  if not alive:
    print(f"Sadly, you died fighting the {monster}.")
  else:
    return locationB # You could always ask them which way to go

def locationB():
  print("Phew, you lived to see another day")

# Start the game
print("Welcome to my adventure game...")
location = locationA

while location:
  location = location()

print("GAME OVER")
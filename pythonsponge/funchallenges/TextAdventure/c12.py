def locationA(): # ruined castle
  print("You are in a ruined castle, just inside the gatehouse.")
  print("There is a building to the North and a walled area to the East.")
    
  print("Which way do you want to go?")
  choice = input()
    
  if choice == "N":
    return locationB # This line moves you to location B from location A
  elif choice == "E":
    return locationC # This line moves you to location C from location A
  elif choice == "S":
    print("strangely, when you go South you end up back where you started...")
    return locationA
  else:
    print("You cannot go that way...")
    return locationA

def locationB(): # the great hall
  print("You are in the great hall.")
    
def locationC(): # the keep
  print("You are in the keep.")       
    
# Start the game
print("Welcome to my adventure game...")
location = locationA

while location:
  location = location()

print("GAME OVER")
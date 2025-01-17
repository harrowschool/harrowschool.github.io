def locationA(): # ruined castle 
  print("You are in a ruined castle, just inside the gatehouse.") 
  print("You spot a bridge to the North.")    

  print("Which way do you want to go (N/S/E/W)?") 
  choice = input().upper()

  if choice == "N":
    return locationB # This line moves you to location B from location A 
  else:
    print("strangely, when you go that way you end up back where you started...")
    return locationA

def locationB(): # the bridge of death - modify to make appropriate to your game.
  print("You have arrived at the bridge of death where you must answer five, no three questions:")
  
  choice = input("What is your name? ")
  if choice.lower() != "sir lancelot of camelot":
    print("bad luck, you perish!")
    return
  
  choice = input("What is your quest? ") 
  if choice.lower() != "to seek the holy grail": 
    print("bad luck, you perish!")
    return 

  ______ = input("What is your favourite colour? ") 
  if choice.l____() != "blue": 
    print("___________________")
    r_____    

  print("Off you go then...") 
  return locationC  

def locationC(): # the keep 
  print("You are in the keep and have survived.")     

# Start the game 
print("Welcome to my adventure game...") 
location = locationA  

while location: 
  location = location()  

print("GAME OVER") 
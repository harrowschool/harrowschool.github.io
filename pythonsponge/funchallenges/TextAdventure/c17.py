def ruinedCastle():
  print("You are in a ruined castle, just inside the gatehouse.") 
  print("There is a building to the North and a walled area to the East.") 
  print("Which way do you want to go (N/E)?") 
  choice = input()    

  #### NEW CODE USING A DICTIONARY FOR DIRECTIONS #### 

  directions = {"N": theGreatHall, "E": theKeep}

  # check their first letter of input in uppercase
  letter = choice[0].upper()
  if letter in d_________:
    return directions[______] 
  else: 
    print("strangely, when you go in that direction you end up back where you started...")
    return ruinedCastle

  #### END OF NEW CODE #####  

def theGreatHall():
  print("You are in the great hall and have survived...well done!")      

def theKeep(): 
  print("You are in the keep where you perish...bad luck!")           

# Start the game 
print("Welcome to my adventure game...") 
location = ruinedCastle 

while location: 
  location = location() 

print("GAME OVER") 
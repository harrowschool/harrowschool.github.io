import random

gameOver = False

while not gameOver:

  Player = input("Enter choice R (rock), P (paper) or S (scissors): ")

  # ==> TASK: FIX THIS NEXT LINE; IT DOESN'T LOOK QUITE RIGHT!
  Computer = random.randint(1,4) 
  
  # Changing the random number into a letter
  if Computer == 1:
    Computer = "R"
  elif Computer == 2:
    Computer = "P"
  else:
    Computer = "S"

  # ==> TASK: FIX THIS NEXT LINE; IT ALWAYS SEEMS TO PRINT THE SAME CHOICE FOR BOTH COMPUTER & PLAYER
  print("Player  has picked", Player, "and Computer has picked", Player)
  
  # ==> THIS NEXT LINE DOESN'T SEEM TO BE WORKING!
  if Player == "Computer":     # if they both picked the same thing
    print("Draw! Try again")   # they draw
    continue                   # so skip the next section and restart the loop

 # find the winner
  if Player == "R":
    if Computer == "S":
      print("Player wins!")
    else:
      print("Computer wins!")
  elif Player == "P":
    if Computer == "R":
      print("Player wins!")
    else:
      print("Computer wins!")
  else:
    # ==> TASK: NOT SURE THIS NEXT LINE HAS THE RIGHT WINNER; FIX IT!
    if Computer == "R":
      print("Player wins!")
    else:
      print("Computer wins!")

  # quit the loop
  gameOver = True
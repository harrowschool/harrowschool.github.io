# O Christmas Tree
import random

# CHALLENGE 1
# ==> Allow the user to input their own value for the height
height = 5

for y in range(height):

  print(" " * (height - y), end="")
    
  # CHALLENGE 2
  # ==> The Christmas tree is looking very lop-sided.
  
  for x in range(y+1):
    # CHALLENGE 3
    # ==> Having only X's is somewhat bland.
    symbol = random.choice(["X"])
    
    # CHALLENGE 4
    # ==> The tree needs a star at its peak.
    if False:
      symbol = "★"
      
    if symbol == "X":
    
      # ==> USED IN EXTENSION CHALLENGE
      if False:
        symbol = ">"
      elif False:
        symbol = "<"

    print(symbol, end="")
    
  print()

print(" " * height + "|")

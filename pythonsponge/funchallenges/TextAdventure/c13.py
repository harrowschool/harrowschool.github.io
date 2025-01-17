# Python lists: https://www.w3schools.com/python/python_lists.asp
# List methods: https://www.w3schools.com/python/python_ref_list.asp

Knapsack = []

def locationA():
  print("Some location.... that may or may not contain a candle")
  
  if "Candle" not in Knapsack:
    choice = input("You spot a candle on the floor, do you wish to take it (y/n)? ")
    if choice.lower().startswith("y"):
      Knapsack._____________("candle")
  return locationB
  
def locationB():
  print("You are in a dark cave... some light would be helpful!")
  if "______" in Knapsack:
    print("You use your candle and can see your way to the exit. Humanity is saved.")
  else:
    print("It is dark, you fell into a pit and died.")


# Start the game
print("Welcome to my adventure game...")
location = locationA

while location:
  location = location()

print("GAME OVER")
import random

again = True

while again:
  roll = random.randint(1, 6)
  print("I rolled my die and got", roll)
  again = (input("again (y/n)? ").lower() == "y")
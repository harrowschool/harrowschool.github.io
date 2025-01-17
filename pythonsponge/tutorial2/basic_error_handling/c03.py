myFruits = ["apple", "banana", "pear", "orange", "grape", "strawberry"]

try:
  choice = int(input("enter a fruit number from 1 to 6 inclusive: "))
  index = choice - 1
  fruit = myFruits[index]
  print("my fruit in that position in my favourites list is", fruit)
except Exception as e:
  print("this was the error that I detected:")
  print(e)
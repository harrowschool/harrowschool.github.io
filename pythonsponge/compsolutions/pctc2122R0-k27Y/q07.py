burger = input()
 
if burger == "carrot" or burger == "lettuce":
  price = 50
  ketchup = input()
  if ketchup == "y":
    price = price + 15
else:
  price = 70
  
gerkins = int(input())
price = price + gerkins * 5
print(price)

'''
# ALSO OF INTEREST...

burger, option = input(), input()
 
if burger in ["carrot", "lettuce"]:
  print(50 + 15 * (option == "y") + 5 * int(input()))
else:
  print(70 + 5 * int(option))


'''
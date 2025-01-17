# Complete these challenges to try and fill out all five stars :)
numbers = [1, 5, -1, 4, 29, 15, 3]

# ----- CHALLENGE 1 -----
# We want to sum all of these numbers
# (like adding them all on a calculator)
# Here we want to add up total to equal the total of our numbers!

total = 0

for value in numbers:
  # TASK => CHANGE THE NEXT LINE - we need to add to the total. What do we do to add to the total?
  total = 0

print ("Calculated total to be:", total)

# ----- CHALLENGE 2 -----
# Now we want to find the PRODUCT of all these numbers
# (as if we multiply them all together on a calculator)

product = 1 #we need to start with 1 here, or we would just be multiplying 0!

for value in numbers:
  # TASK => CHANGE THE NEXT LINE - we need to multiply the product by the new number
  product = 0

print("Calculated the product to be:", product)

#----- CHALLENGE 3 -----
# We have a list of operations e.g. multiplying or adding
operations = ["+","-","*","-","+","*"]

# Now we want to use these operations 'between' our list numbers
opTotal = numbers[0] # We just start with our first number

for i in range(len(numbers)-1):
  value = numbers[i+1] # Here we get the next value to use
  op = operations[i] # Here we get the next operation to use
  if op == "+":
    opTotal = 0 # TASK => CHANGE THIS LINE, this is the same as Challenge 1!
  elif op == "*":
    opTotal = 0 # TASK => CHANGE THIS LINE, this is the same as Challenge 2!
  elif op == "-":
    opTotal = 0 # TASK => CHANGE THIS LINE, how do we subtract?

print("Calculated result to be:", opTotal)

# ----- CHALLENGE 4 -----
# We now want to make a NEW LIST which has the SQUARE of all of the original numbers

numbers2 = []
for value in numbers:
  # TASK => CHANGE THE NEXT LINE - what should be added to the new list?
  numbers2.append(0)

print("Your new numbers are", numbers2)

# ----- CHALLENGE 5 -----
# The final challenge!
# Computers store data in 1s and 0s (binary)
# We need to create a FINAL LIST which contains the 8-BIT binary form (as strings) for all our original numbers

numbers3 = []

for value in numbers:
  # TASK => you need to change the next line ... but to what?
  bin_num = f"{0:08b}"
  numbers3.append(bin_num)    
    
print("The combined binary is:", numbers3)

# DON'T CHANGE THIS CODE - here your stars are calculated & printed!
from math import prod
stars = sum([total==sum(numbers),product==prod(numbers),"\u0032\u0034"==str(opTotal)[::-1],sum(numbers2)==1118 and prod(numbers2)==681210000,"".join(numbers3).count("1") in [15,20]])
if stars==5: print("Well done! You got all five stars!")
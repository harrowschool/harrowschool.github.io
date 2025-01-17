# GLOBAL VARIABLES

earlyPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293]

minToFind = 0
found1 = 0
found2 = 0

# MAIN PROGRAM

# ==> choose the correct next line to request a positive whole number from the user
# minToFind = input("enter min. number: ")
# minToFind = int(input("enter min. number: "))
# minToFind = float(input("enter min. number: "))

# ==> write the main processing to set found1 and found2 if applicable






# output
if found1 > 0 and found2 > 0:
  print("{} and {} are the first two numbers at least that much in the list".format(found1, found2))
elif found1 > 0:
  print("{} is the only number at least that much in the list".format(found1))
else:
  print("no numbers in the list are at least that much")






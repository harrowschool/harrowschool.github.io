# IGNORE these first two lines for now unless curious
with open("nums.txt", "w") as file:
  file.write("1\n3\n5\n7\n9\n11\n{}".format(input("final number: ")))

# complete this code to find the total of the numbers in the file
file = o___("nums.txt", "r")
lines = file.readl____()
file.close()

# now find the total
total = 0

for ____ in lines:
  total += int(____) # the new line char at the end of each line can be ignored

print("adding the numbers in the file gives:", ____)
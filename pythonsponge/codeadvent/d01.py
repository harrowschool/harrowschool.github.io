# here is some test data you can use to check you get the same answer as shown on the right
data = '''4
6
5
3
2
8
9'''.splitlines()

# uncomment these three lines to use the real challenge data instead when ready
# file = open("d01.txt", "r")
# data = file.readlines()
# file.close()

# set funds to Santa's initial amount of money
funds = ___________

# loop through each line of the data
count = 0
while count < len(data):
    line = data[count]
    # turn the line into an integer and subtract it from funds
    funds = funds - int(___)
    count = count + 1

# print the final amount of money Santa has
print(_____)

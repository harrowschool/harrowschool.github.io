###########################
# GLOBAL VARIABLES
###########################

data = []
lastChar = ""
position = 0

###########################
# MAIN PROGRAM
###########################

# data setup

# use example data for testing
data = list('GZFD')

# uncomment these two lines to use the real challenge data instead when ready
# with open("data.txt", "r") as datafile:
#    data = list(datafile.read().strip())

# ==> COMPLETE THIS MAIN PROCESSING LOOP TO REDUCE THE LIST TO 2 SINGLE CHARACTERS
while len(data) > 2:
    lastChar = data.pop()
    position = ord(lastChar) - ord('A')
    print(position)

# print the final output
print("".join(data))

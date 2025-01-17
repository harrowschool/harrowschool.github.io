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

# uncomment these three lines to use the real challenge data instead when ready
# file = open("d06.txt", "r")
# data = list(file.read().strip())
# file.close()

# ==> COMPLETE THIS MAIN PROCESSING LOOP TO REDUCE THE LIST TO 2 SINGLE CHARACTERS
while len(data) > 2:
    lastChar = data.pop()
    position = ord(lastChar) - ord('A')
    print(position)

# print the final output
print("".join(data))

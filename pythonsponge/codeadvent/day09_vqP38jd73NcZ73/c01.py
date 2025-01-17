###########################
# LIBRARIES
###########################

import string

###########################
# CONSTANTS
###########################

# setup a string of the uppercase alphabet A-Z to avoid typing them all in
ALPHABET = string.ascii_uppercase

###########################
# GLOBAL VARIABLES
###########################

data = 0
send_to_end = True
elves_line = []
middle = 0
extract = ""

###########################
# MAIN PROGRAM
###########################

# data setup

# use example data for testing
data = 5

# uncomment these two lines to use the real challenge data instead when ready
# with open("data.txt", "r") as datafile:
#   data = int(datafile.read())

# setup the 19 letters
elves_line = list(ALPHABET[:19])

# main processing loop for the required number of movements
# filling in these gaps will work but the senior researcher fears it may be too slow for large numbers
# ==> COULD THERE BE A WAY OF SPEEDING IT UP
# ==> E.G. BY FIRST FINDING HOW MANY MOVEMENTS BEFORE THEY GET BACK TO WHERE THEY STARTED?
for count in range(data):
    middle = len(elves_line) // 2
    extract = elves_line.pop(______)
    if send_to_end:
        elves_line.append(_______)
    else:
        elves_line.insert(0, _______)
    send_to_end = not send_to_end

# print the final output
result = "".join(elves_line)
print(result)

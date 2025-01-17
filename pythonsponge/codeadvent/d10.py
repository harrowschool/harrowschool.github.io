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
result = ""

###########################
# SUBPROGRAMS
###########################


def get_nth_tri_num(n):
    return sum((x for x in range(n+1)))


def hash(row):

    # local variables
    code, number_made = row.split(" ")
    pos = 0
    tri = 0

    # ==> COMPLETE THE HASH LOGIC IN THIS PROCESSING LOOP & BELOW

    for ch in code:
        if not ch.isdigit():
            pos = ALPHABET.index(ch) + 1
            tri = get_nth_tri_num(pos)

    # ==> CHANGE TO RETURN THE CALCULATED LETTER
    return "-"

###########################
# MAIN PROGRAM
###########################

# data setup


# use example data for testing
data = ["B4G7 257"]

# uncomment these three lines to use the real challenge data instead when ready
# file = open("d10.txt", "r")
# data = [line.strip() for line in file.readlines()]
# file.close()

# main processing comprehension
result = "".join([hash(row) for row in data])

# print the final output
print(result)

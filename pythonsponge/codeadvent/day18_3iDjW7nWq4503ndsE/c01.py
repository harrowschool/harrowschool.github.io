###########################
# GLOBAL VARIABLES
###########################

data = ""
city = ""
magic_seed = 0

###########################
# SUBPROGRAMS
###########################


def calc_magic_dust_weight(pCity, pMagic_seed):
    # Convert each letter to its alphabetic position
    letter_positions = [ord(char.upper()) - ord('A') + 1 for char in pCity]

    # ==> COMPLETE THE GAP TO CALC THE PRODUCT OF THE LETTER POSITIONS
    product = 1
    for pos in letter_positions:
        product *= ___

    # Sum the weights for each letter
    total = 0

    # ==> COMPLETE THE GAP TO CALC THE SUM OF THE WEIGHTS
    # ==> BUT YOU MIGHT STILL FIND IT TOO SLOW FOR THE REAL DATA!
    for pos in letter_positions:
        result = 0
        for count in range(pMagic_seed):
            result = (result + ___) * ___
        total += result % 999

    return total

###########################
# MAIN PROGRAM
###########################


# data setup - use example data for testing
data = '''\
BO
1000'''.splitlines()

# uncomment these two lines to use the real challenge data instead when ready
# with open("data.txt", "r") as datafile:
#     data = [line.strip() for line in datafile.readlines()]

# ==> COMPLETET TO GET THE CITY AND THE MAGIC SEED FROM THE DATA
city = data[_]
magic_seed = int(data[_])

# Find the summary binary sequence
print(calc_magic_dust_weight(city, magic_seed))

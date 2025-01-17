###########################
# GLOBAL VARIABLES
###########################

valid = 0
data = []

###########################
# SUBPROGRAMS
###########################

# ==> IMPLEMENT THIS FUNCTION


def isValid(row):
    print("validating...", row)
    return True

###########################
# MAIN PROGRAM
###########################

# data setup


# use example data for testing
data = '''1834,2643,4952,4588,6
5744,2699,5992,3221,3'''.splitlines()

# uncomment these three lines to use the real challenge data instead when ready
# file = open("d07.txt", "r")
# data = [line.strip() for line in file.readlines()]
# file.close()

# data setup - convert data to 2D list
data = [line.split(",") for line in data]

for row in data:
    # ==> CALL THE VALIDATIONG FUNCTION TO CHECK
    if _______(row):
        valid += 1

# print the number of valid records found
print(valid)

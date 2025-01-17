###########################
# GLOBAL VARIABLES
###########################

total = 0
remainder = 0
data = []

###########################
# SUBPROGRAMS
###########################


def convert_from_base_12(num_string):
    total = 0

    # ==> REPLACE THIS LOOP WITH A CALCULATION LOOP
    for ch in num_string:
        print(ch)

    return total

###########################
# MAIN PROGRAM
###########################

# data setup


# use example data for testing
data = '''3X2Y9
7YY429
31554
X1288Y
3000X'''.splitlines()

# uncomment these three lines to use the real challenge data instead when ready
# file = open("d05.txt", "r")
# data = [line.strip() for line in file.readlines()]
# file.close()

# main processing loop to convert each line back from base-12 and add
for line in data:
    total += convert_from_base_12(line)

# ==> WRITE THE NEXT LINE TO FIND REMAINDER WHEN DIVIDED BY ONE MILLION

# print the final output
print(remainder)

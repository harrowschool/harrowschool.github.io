###########################
# IMPORT LIBRARIES
###########################

import math

###########################
# GLOBAL VARIABLES
###########################

data = []
total_paper_area = 0.0

###########################
# MAIN PROGRAM
###########################

# data setup

# use example data for testing
data = '''10x12x6
5x8x3
15x4x9'''.splitlines()

# uncomment these three lines to use the real challenge data instead when ready
# file = open("d03.txt", "r")
# data = file.readlines()
# file.close()

# main processing loop for all presents
for line in data:

    # Split the dimensions on the letter x and convert all to integers
    # ==> COMPLETE THE BLANK IN THE NEXT LINE
    dimensions = line.strip().split('_')

    width = int(dimensions[0])
    depth = int(dimensions[1])
    # ==> ADD A LINE BELOW TO CONVERT THE LAST DIMENSION

    # ==> COMPLETE THE CALCULATION TO FIND THE PRESENT SURFACE AREA
    surface_area = 2 * width * depth + 2 * ___________________________________

    # find 20% extra paper for overlap and wastage
    extra = surface_area / 100 * 20
    # ==> COMPLETE THE NEXT LINE
    paper_needed = surface_area + _____

    # ==> ADD A LINE BELOW TO INCREASE THE RUNNING TOTAL OF total_paper_area

# round UP to next one hundred
hundreds = total_paper_area / 100
# ==> COMPLETE THE NEXT LINE
hundreds = math.ceil(________)
total_paper_area = hundreds * 100

# ==> ADD A LINE BELOW TO PRINT THE FINAL ANSWER

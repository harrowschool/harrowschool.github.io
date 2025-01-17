###########################
# GLOBAL VARIABLES
###########################

sprouts = 0
field = []
data = []

###########################
# MAIN PROGRAM
###########################

# data setup

# use example data for testing
data = '''.....
.P...
..P..
.....'''.splitlines()

# uncomment these three lines to use the real challenge data instead when ready
# file = open("d08.txt", "r")
# data = [line.strip() for line in file.readlines()]
# file.close()

# field setup - convert data to 2D list
field = [list(line) for line in data]

# ==> COMPLETE THE FIVE GAPS IN THE PROCESSING LOOP TO ADD SPROUTS TO THE FIELD
for y in range(len(field)):
    for x in range(len(field[0])):
        if field[y][x] == "_":
            for chx, chy in [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (__, __)]:
                if 0 <= x+chx < len(field[0]) and 0 <= y+chy < len(field) and field[y+chy][x+chx] != "_":
                    field[y+chy][x+chx] = "_"

# ==> ADD A NESTED LOOP HERE TO COUNT THE NUMBER OF SPROUTS IN THE 2D LIST


# print the final output
print(sprouts)

###########################
# CONSTANTS
###########################

START_X = 1
START_Y = 1

###########################
# GLOBAL VARIABLES
###########################

trail_sum = 0
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
last = (-1, -1)
curr_dir_idx = 0
x = START_X
y = START_Y

###########################
# MAIN PROGRAM
###########################

# data setup - use example data for testing
data = '''\
.......
.@.@@@.
.@.@.@.
.@@@@@.
...@...
...@...
.......'''.splitlines()

# uncomment these two lines to use the real challenge data instead when ready
# with open("data.txt", "r") as datafile:
#     data = [line.strip() for line in datafile.readlines()]

while True:

    # Check all four directions for the next '@'
    found = False

    for count in range(4):

        # always try current direction first
        dx, dy = directions[curr_dir_idx]
        new_x, new_y = x + dx, y + dy

        # ==> TEST IF new_x and new_y are all of the following...
        # in range for the grid, contains an "@" and is not the same as last

        # ==> if so then update last, set x,y to the new_x, new_y
        # ... and update the trial sum, set found to True and break

        curr_dir_idx = (curr_dir_idx + 1) % 4

    # once directions checked
    if not found:
        break

# Output the trail sum
print(trail_sum)

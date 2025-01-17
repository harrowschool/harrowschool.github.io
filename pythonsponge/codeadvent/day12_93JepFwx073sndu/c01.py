###########################
# GLOBAL VARIABLES
###########################

total = 0

###########################
# SUBPROGRAMS
###########################

def is_border(data, x, y):
  # return True if the cell at (x,y) is bordered by at least one . in any direction including diagonals
  
  moves = [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)]
  
  for chx, chy in moves:

    # ==> COMPLETE TO ADD ON THIS POSSIBLE MOVE TO THE CELL (x,y) BEING CONSIDERED
    cell_x = x + ___
    cell_y = y + ___

    # ==> COMPLETE THESE GAPS SO THAT IF BOTH cell_y AND cell_x are valid for the grid dimensions
    # and you've found a . then return True otherwise once the loop is over and not found return False

    if 0 <= cell_y < len(data) and ___________________:
      if data[cell_y][cell_x] == "_":
        return ____

  return _____

###########################
# MAIN PROGRAM
###########################

# data setup

# use example data for testing
data = '''\
........................
.XXXXXX....XXXXX..XXX...
.XXXXXX....XXXXX..XXX...
.XXXXXXXXXXXXXXXXXXXXXX.
.XXXXXXXXXXXXXXXXXXXXXX.
.XXXXXXXXXXXXXXXXXXXXXX.
.XXXXXXXXXXXXXXXXXXXXXX.
.XXXXXX.........XXXXXXX.
.XXXXXX.........XXXXXXX.
........................'''.splitlines()

#uncomment these two lines to use the real challenge data instead when ready
# with open("data.txt", "r") as datafile:
#    data = [line.strip() for line in datafile.readlines()]

# setup data
data = [list(line) for line in data]

for y in range(len(data)):
  for x in range(len(data[0])):
    # ==> COMPLETE THE TWO GAPS BELOW
    if data[y][x] == "_" and ________(data, x, y):
      total += 1

print(total)


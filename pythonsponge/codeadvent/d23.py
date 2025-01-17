###########################
# CONSTANTS
###########################

DISTANCE_LIMIT = 10

###########################
# GLOBAL VARIABLES
###########################

coordinates = []
clusters = []
data = ""

###########################
# SUBPROGRAMS
###########################

def manhattan_distance(coord1, coord2):
    return abs(coord1[0] - coord2[0]) + abs(coord1[1] - coord2[1])

def add_to_cluster(coord, clusters):
  # ==> IMPLEMENT THIS FUNCTION
  # first find all clusters which this new coordinate can add to
  # if none then make a new cluster group for it, add it and add the group to clusters
  # if one then just add it to that cluster group
  # if more than one then merge those two cluster groups and add it
  

###########################
# MAIN PROGRAM
###########################

# data setup - use example data for testing
data = '''\
10,10
15,15
13,14
40,50
45,55'''.splitlines()

# uncomment these three lines to use the real challenge data instead when ready
# file = open("d23.txt", "r")
# data = [line.strip() for line in file.readlines()]
# file.close()    

# coordinate setup
coordinates = []
for line in data:
  x, y = line.split(",")
  coordinates.append((int(x), int(y)))

# main loop to add all coordinates to clusters
for coord in coordinates:
    add_to_cluster(coord, clusters)

# Output the number of clusters
print(len(clusters))



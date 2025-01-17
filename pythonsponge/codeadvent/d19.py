###########################
# GLOBAL VARIABLES
###########################

data = []
stones = []
intensities = []
total = 0

###########################
# MAIN PROGRAM
###########################

# data setup - use example data for testing
data = '''\
7
3
5'''.splitlines()

# uncomment these three lines to use the real challenge data instead when ready
# file = open("d19.txt", "r")
# data = [line.strip() for line in file.readlines()]
# file.close()

# setup the stones
stones = [int(stone) for stone in data]

# we build up the intensities we need from the start upwards so find the max
max_stone = max(stones)

# base case intensities for stones marked 0 to 3
intensities = [1, 1, 1, 1]

# Build up solutions iteratively - dynamic programming
# ==> COMPLETE THESE NEXT TWO LINES
for n in range(4, _________ + 1):
    ___________.append(intensities[-1] +
                       ___________________________________________)

# Calculate the total intensity for the given stones
# ==> COMPLETE THIS LINE
total = sum(intensities[_____] for stone in ______)

# Output the result
print(total)

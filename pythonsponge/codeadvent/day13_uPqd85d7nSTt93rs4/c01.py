###########################
# GLOBAL VARIABLES
###########################

# current sleigh position
x = 0
y = 0

# current direction - starts facing North
chx = 0
chy = -1

# the list of all points visited initially only included [0, 0]
houses = [[0, 0]]

###########################
# MAIN PROGRAM
###########################

# data setup

# use example data for testing
data = '''\
12
L
18
R
4
R
2
R
12
L
5
L
14'''.splitlines()

# uncomment these two lines to use the real challenge data instead when ready
# with open("data.txt", "r") as datafile:
#     data = [line.strip() for line in datafile.readlines()]


# process every movement instruction
for inst in data:

    if inst == "L":

        # here are the rules for updating the direction the sleigh is facing for a left turn based on the current direction
        if chx == 0 and chy == -1:
            chx = -1
            chy = 0
        elif chx == -1 and chy == 0:
            chx = 0
            chy = 1
        elif chx == 0 and chy == 1:
            chx = 1
            chy = 0
        else:
            chx = 0
            chy = -1

    elif inst == "R":
        # ==> COMPLETE THE SIMILAR CODE FOR RIGHT TURNS BELOW
        if chx == 0 and chy == -1:
            chx = 1
            chy = 0

    else:

        # ==> COMPLETE THE CODE BELOW FOR THE FORWARD MOVES, ADDING NEW HOUSES TO THE LIST OF HOUSES VISITED
        for count in range(int(inst)):

            x += chx
            y += ___

            if [x, y] not in ______:
                houses.append([x, y])


# output the number of houses visited
print(len(houses))

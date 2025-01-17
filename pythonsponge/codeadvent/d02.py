# here is some test data you can use to check you get the same answer as shown on the right
data = '09518590'

# uncomment these three lines to use the real challenge data instead when ready
# file = open("d02.txt", "r")
# data = file.readline().strip()
# file.close()

# create list of booleans to represent the lights
# you can swap this next line to lights = [False] * 10 if you prefer!
lights = [False, False, False, False, False, False, False, False, False, False]

# loop over each character to find which light to toggle & change it
for ch in data:
    light_position = int(ch)
    # ==> ADD CODE HERE TO TOGGLE THAT LIGHT

# build the final light display
result = ""
for light in lights:
    if light == True:
        # ==> COMPLETE THIS NEXT LINE
        result += ___
    else:
        # ==> COMPLETE THIS NEXT LINE
        result += ___

# output the answer
# ==> ADD A FINAL LINE BELOW

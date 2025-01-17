# CONSTANTS
FILENAME = "numbers.txt"

# GLOBAL VARIABLES
total = 0
myFile = None

# ==> initialise any additional global variables used

# MAIN PROGRAM

# first find the total of the existing numbers using read mode
myFile = open(FILENAME, "r")

for line in myFile:
  line = line.strip()
  # ==> complete the next line
  total += int(______)

# close the file to re-open it in append mode
myFile.close()

# ==> now open the file in append mode to add on the total on a new line
myFile = open(_________, ___)

# ==> write the required new-line character and total


# close the file
myFile.close()
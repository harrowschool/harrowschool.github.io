# CONSTANTS

FILENAME = "data.txt"

# GLOBAL VARIABLES
oldLines = []
newLines = []

# ==> initialise any additional global variables used

# SUBPROGRAMS

def getLinesAsList(filename):
  myFile = open(filename, "r")
  result = myFile.readlines()
  myFile.close()
  return result

def writeLinesAsList(filename, lst):
  myFile = open(filename, "w")
  # ==> complete the next line to write the contents of the list to the file
  myFile.writelines(___)
  myFile.close()

# MAIN PROGRAM

oldLines = getLinesAsList("data.txt")

# ==> complete the processing to add just the first & last items of oldLines to newLines
newLines.append(_____________)
newLines.append(_____________)

# ==> add a call to the writeLinesAsList subprogram to write the contents of newLines to overwrite the contents of data.txt


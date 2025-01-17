# CONSTANTS

FILENAME = "fibonacci.txt"

# GLOBAL VARIABLES

sequence = [0, 1]
numOfTerms = 0

# ==> initialise any additional global variables used

# SUBPROGRAMS

def fillSequence(lst, n):
  
  # ==> choose the correct next line to avoid a logical error
  # while len(lst) < n:
  # while len(lst) <= n:
    
    # ==> fill in the gaps to complete the Fibonacci sequence to increase the list to contain n terms
    nextTerm = lst[-1] + lst[___]
    lst.append(________)

# ==> complete the subprogram to write the contents of the list to the file, one per line
def writeFile(lstOfNumbers, filename):
  prefix = ""
  nextLine = ""
  myFile = open(filename, "__")
  for num in lstOfNumbers:
    nextLine = "{}{}".format(prefix, ________)
    # ==> write the line to the file
    _________________________
    prefix = "\n"
  myFile.close()

# MAIN PROGRAM

# input a positive integer greater than 2
numOfTerms = int(input("enter a positive integer larger than 2: "))
fillSequence(sequence, numOfTerms)
writeFile(sequence, FILENAME)
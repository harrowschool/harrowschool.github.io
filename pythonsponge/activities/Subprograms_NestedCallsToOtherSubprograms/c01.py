# CONSTANTS

WIDTH = 10

# GLOBAL VARIABLES

numbers = [12.172, 8.943, 7.486, 11.251, 9.782, 13.936, 8.214, 4.778, 14.381]

# SUBPROGRAMS

def makeTopBottomLine(pWidth):
  print("+" + "-" * pWidth + "+")

def makeTableEntry(pNum, pWidth):
  print("|{:^{}.1f}|".format(pNum, pWidth))

def makeTable(pNumbers, pWidth):
  # ==> add code to call the other sub-programs below by replacing each placeholder below
  ___________________________

  for num in pNumbers:
    ___________________________

  ___________________________


# MAIN PROGRAM

# ==> call the makeTable subprograme to generate the requested table
makeTable(numbers, WIDTH)

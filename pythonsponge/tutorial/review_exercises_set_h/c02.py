MONTHS = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]

def addSomeMonths(currMonth):
  monthIndex = MONTHS.index(currMonth)
  add = int(input("jump how many months?"))
  monthIndex = (monthIndex + ___) % ___(______)
  return MONTHS[__________]	

currMonth = "JAN"
newMonth = addSomeMonths(_________)

print("the new month is:", ________)

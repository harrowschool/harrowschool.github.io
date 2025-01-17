# GLOBAL VARIABLES

# FIELDS ARE STOCK ID AND QUANTITY IN STOCK
# RECORDS ORDERED BY ID ASCENDING
stockRecords = [
  ["APK03", 17], 
  ["BEM02", 5], 
  ["BUR12", 12], 
  ["DAK07", 9], 
  ["FUL05", 4],  
  ["MER11", 9],  
  ["PBM04", 15],  
  ["RIQ01", 8],  
  ["SEP06", 10],  
  ["STU02", 19],  
  ["UAI08", 2],  
  ["VAR06", 4],  
  ["VET03", 8],  
  ["WAS06", 4],  
  ["WEY12", 7],  
  ["XIW07", 7],  
  ["YOR02", 4],  
  ["ZEE11", 18]
  ]

stockResult = -1
comparisonsMade = 0
searchID = ""

# MAIN PROGRAM

# input the age to search for - assume an integer provided
searchID = input("enter a product ID to search for: ")

# ==> complete a processing loop which quits once the item is found or the position it would be has been passed
# ==> incrememt comparisonsMade each time around the loop

  comparisonsMade = comparisonsMade + 1


# output
if stockResult == -1:
  print("{} comparisons were made but a product with that ID was not found".format(comparisonsMade))
else:
  print("After {} comparisons the product was found which has stock quantity {}".format(comparisonsMade, stockResult))



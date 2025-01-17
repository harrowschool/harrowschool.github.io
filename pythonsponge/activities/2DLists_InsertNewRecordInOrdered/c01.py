# GLOBAL VARIABLES

# FIELDS ARE ID AND QUANTITY IN STOCK
# RECORDS ORDERED BY ID ASCENDING
stockRecords = [["APK03", 17], ["BEM02", 5], ["BUR12", 12], ["DAK07", 9], ["FUL05", 4],  ["MER11", 9],  ["PBM04", 15],  ["RIQ01", 8],  ["SEP06", 10],  ["STU02", 19],  ["UAI08", 2],  ["VAR06", 4],  ["VET03", 8],  ["WAS06", 4],  ["WEY12", 7],  ["XIW07", 7],  ["YOR02", 4],  ["ZEE11", 18]]

newProductID = ""
enteredStockQuantity = ""
newStockQuantity = -1
completed = False
index = 0

# ==> initialise any additional global variables used

# MAIN PROGRAM

# input the new product ID to insert
newProductID = input("enter a product ID to add: ")

# ==> rearrange these lines to continually input a new stock quantity until a valid positive integer is entered
# REARRANGE SECTION - USE ALT & UP/DOWN ARROWS TO REARRANGE A LINE
  else:
    print("invalid stock quantity...please try again")
    newStockQuantity = int(enteredStockQuantity)
  enteredStockQuantity = input("enter stock quantity as a positive integer: ")
while newStockQuantity == -1:
  if enteredStockQuantity.isdigit() == True and int(enteredStockQuantity) > 0:
# END OF REARRANGE SECTION #

# ==> complete a processing loop to find the correct location for the new record and insert it
while completed == False and index < len(stockRecords):


# ==> add code to append the new record onto the end of the list if it still hasn't been inserted
if completed == False:


# output the updated list of records
print(stockRecords)



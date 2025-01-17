import datetime

day_correct = False

while day_correct == False:

    day = int(input("Enter the day that you were born 1-31: "))

    month =  int(input("Enter the month that you were born 1-12: ")) 

    # ==> WHOOPS, DECEMBER DOESN'T HAVE 30 DAYS, REMOVE 12 from this LIST
    if month in [4, 6, 9, 11, 12]: 
        # months with 30 days
        if day > 30 or day < 1:
            print("That's not a day in that month!")
        else:
            day_correct = True
    else:
        # months with 31 days
        if day > 31 or day < 1:
            print("That's not a day in that month!")
        else:
            day_correct = True
    # ==> HMMM, WE SEEM TO BE MISSING FEBRARY WHICH HAS 1-29 DAYS - HOW TO FIX?

year = int(input("Enter the year that you were born (fully, e.g: 2011): "))

birth = datetime.datetime(year, month, day)

# ==> WHOOPS, SEPTEMBER BIRTHDAYS WOULD GO INTO THE NEXT ACADEMIC YEAR - FIX THIS
if birth.month in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    graduateSixthForm = birth.year + 18
else:
    graduateSixthForm = birth.year + 19

print("You will graduate from Sixth Form in: ")
print("July", graduateSixthForm)

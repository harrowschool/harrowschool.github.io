import datetime

# create a new date object for the 1st of January 2001
new_millenium = datetime.date(2001, 1, 1)

# you can also create it from a string in different ways
new_millenium = datetime.date.fromisoformat('2001-01-01')
new_millenium = datetime.date.strptime('2001-01-01', '%Y-%m-%d')

print("the first day of the new millenium was a:")
print(new_millenium.strftime('%A'))


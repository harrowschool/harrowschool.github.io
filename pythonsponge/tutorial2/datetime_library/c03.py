from datetime import datetime as dt, timedelta as td

rightNow = dt.now()
quarterHour = td(minutes=15)

print("right now it is:", rightNow.strftime('%d %B %H:%M'))
print("but in 15 minutes it will be:", (rightNow + quarterHour).strftime('%d %B %H:%M'))

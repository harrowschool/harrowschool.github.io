from datetime import datetime as dt, timedelta as td
from math import pi

change = td(days = pi)

#start
choice = input("enter datetime as yyyy,mm,dd,hh,mm,ss: ").split(",")
moment = dt(*[int(i) for i in choice])

nextMoment = moment + change

print(f"In pi days times, it will be {nextMoment}")




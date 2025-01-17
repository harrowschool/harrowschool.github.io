DAYS = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

curr_day = "WED"
days_to_add = 1

while days_to_add > 0:
  print("The current day is now", curr_day)
  days_to_add = int(input("enter num. of days to add on or 0 to quit: "))
  if days_to_add > 0:
    curr_pos = DAYS.index(_____________)
    curr_pos += _____________
    curr_pos = curr_pos % len(______)
    curr_day = DAYS[__________]
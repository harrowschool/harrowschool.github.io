sports = []
continuing = True

while continuing:
  sport = input("enter a new sport you like or stop to finish: ")
  if sport.lower() == "stop":
    continuing = False
  else:
    pos = input("enter a position to add it (1,2,3...) or enter end to add to the end: ")
    if pos == "end":
      sports.ap____(_____)
    else:
      sports.insert(int(p__) - 1, _____)

print("your sports list is", sports)
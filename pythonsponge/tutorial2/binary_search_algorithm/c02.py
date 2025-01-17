# ordered data is required for binary search
names = ["Zuya", "Trevor", "Phoebe", "Nicola", "Jack", "Freya", "David", "Barny", "Abigail"]

target = input("Enter a name to search for: ")

low = 0
high = len(names) - 1
found = False

while low <= ____:

  # Note integer division to retain a whole index number
  mid = (low + high) // ___
  
  if names[mid] == ______:
    found = ____
    break
  elif names[mid] > target:
    low = __________
  else:
    high = __________

print("Found!" if found else "Not found...try again!")
from copy import deepcopy

records = [["Jack", 23], ["Maya", 25], ["Emily", 21]]

# a shallow copy
copy1 = list(records)

# another shallow copy by slicing the whole list
copy2 = records[:]

records[0][0] = "Fred"

print("note how they all change...")
print(records)
print(copy1)
print(copy2)

records = [["Jack", 23], ["Maya", 25], ["Emily", 21]]

copy3 = deepcopy(records)

records[0][0] = "Fred"

print("note only records has changed...")
print(records)
print(copy3)
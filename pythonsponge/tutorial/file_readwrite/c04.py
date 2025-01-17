RECORD_LAYOUT = "{0}{1},{2},{3}"

records = [
  ["Lydia", 25, "Ipswich"], 
  ["Max", 31, "Edinburgh"], 
  ["Malita", 57, "Hull"], 
  ["Terry", 45, "Bristol"]
]
  
file = o___("records.csv", "w")

prefix = ""
for record in records:
  ____.write(RECORD_LAYOUT.format(prefix, record[0], record[1], record[2]))
  prefix = "\n"

file.c____()

file = o___("records.csv", "___")

search = input("enter name to search for: ")

for line in f___:
  # split the line from the file up on the commas into a list
  items = line.strip().split(",")
  if items[0].lower() == search.lower():
    next_age = int(items[___]) + 1
    print("FOUND: after their next birthday they will be", next_age)
    break

file.c____()
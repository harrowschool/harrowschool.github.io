name = input("enter a name: ")
LAYOUT = "{0}{1}"

file = open("nameletters.txt", ___)

prefix = ""
for ch in ____:
  file.write(LAYOUT.format(prefix, o__(ch)))
  prefix = "__"

file.close()

# IGNORE these two lines unless curious, just used for automated checking
with open("nameletters.txt", "r") as file:
  print(file.read())
file = open("squares.txt", ___)

n = int(input("how many square numbers would you like to save? "))

prefix = ""
for idx in range(1, n+1):
  file.w____(prefix + str(idx ** 2))
  prefix = "\n"

file.close()

total = 0

file = open("squares.txt", "r")

for line in ____:
  total += int(____.strip())
  
print("All saved, their total is", _____)

file.c____()

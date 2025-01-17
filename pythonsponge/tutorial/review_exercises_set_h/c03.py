# IGNORE these first two lines for now unless curious
with open("chars.txt", "w") as file:
  file.write("\n".join([chr(n) for n in range(52, 95)]))

# complete this code to count how many lines in the file contain only digits.
file = o___("chars.txt", "_")

count = 0

for line in file:
  if line.strip().isd____():
    count += 1

file.c____()

print("count of lines containing only digits:", _____)
file = open("data.txt", "r")

print("here are your three friends still saved...")

for line in file:
  print(line.strip())

file.close()
pack = input()

snaps = 0
index = 0

while index < len(pack) - 1:
  if pack[index] == pack[index+1]:
    snaps += 1
    index += 1
  index += 1

print(snaps)
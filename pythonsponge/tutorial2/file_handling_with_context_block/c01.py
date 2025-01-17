pythag = [3, 4, 5, 5, 12, 13, 7, 24, 25]

with open("pythag.csv", "w") as file:
  for idx in range(0, len(pythag), 3):
    if idx > 0:
      file.write("\n")
    file.write(pythag[idx], pythag[idx+1], pythag[idx+2]")

doubled = [num * 2 for num in pythag]

with open("pythag.csv", "a") as file:
  for idx in range(0, len(doubled), 3):
    file.write("\n")
    file.write(doubled[idx], doubled[idx+1], doubled[idx+2])

print("here are some pythagorean triples:")
with open("pythag.csv", "r") as file:
  print("".join(file.readlines()))
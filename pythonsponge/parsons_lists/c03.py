colours = ["blue", "green", "indigo", "red", "yellow"]
colour = input(f"enter a new colour not in {colours}: ")
index = 0
while index < len(colours):
  if colour < colours[index]:
    break
  index += 1
colours.insert(index, colour)
print("alphabetical colours:", colours)
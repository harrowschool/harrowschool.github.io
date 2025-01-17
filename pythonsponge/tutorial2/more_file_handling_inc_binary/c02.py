icons = [
  ["XXXX", "XOOX", "XOOX", "XXXX"],
  ["XOOX", "OXXO", "OXXO", "XOOX"]
]

# write to file without line breaks
with open("icons.txt", "__") as ____:
  for icon in icons:
    ____.writel_____(icon)

# read the file contents in one go
w___ open("icons.txt", "__") as file:
  all_data = file.read()

# print out all icons with each icon numbered
for idx in range(0, len(all_data), 4):
  if idx % 16 == 0:
    print(f"ICON {idx // 16 + 1}:")
  print(a_______[idx:idx+4])

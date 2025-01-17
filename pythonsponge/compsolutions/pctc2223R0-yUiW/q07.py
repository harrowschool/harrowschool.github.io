size = int(input())
if size % 5 == 0:
  print(str(int(size / 5)) + "x5")
elif size % 4 == 0:
  print(str(int(size / 4)) + "x4")
else:
  print(str(int(size / 3)) + "x3")
  
'''
# ALSO OF INTEREST

size = int(input())

for group in range(5,2,-1):
  if size % group == 0:
    print(f"{size // group}x{group}")
    break

'''
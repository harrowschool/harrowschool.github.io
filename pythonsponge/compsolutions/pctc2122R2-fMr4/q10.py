from itertools import product

BRD_SIZE = 4
board = {i:{} for i in range(BRD_SIZE)}

for i in range(BRD_SIZE ** 2):
  col, row = input()
  board[int(row) - 1]["abcd".index(col)] = (1 if i % 2 == 0 else -1)

def try_three(brd, x, y, dx, dy):
  try:
    if brd[y][x] == brd[y+dy][x+dx] == brd[y+2*dy][x+2*dx]:
      return brd[y][x]
  except:
    pass
  return 0

p1, p2 = 0, 0

for x, y in product(range(0, 4), range(0, 4)):
  for d in ((1,0), (0,1), (1,1), (-1,1)):
    if (score := try_three(board, x, y, *d)) > 0:
      p1 += 1
    elif score < 0:
      p2 += 1

print(f"{p1}-{p2}")
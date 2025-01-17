grid = [list(input()) for _ in range(6)]
diffs = ((1,0), (-1,0), (0,1), (0,-1))

def adjacent_sum(x, y):
  return sum(grid[(y+ch_y) % 6][(x+ch_x) % 6] == '1' for ch_x, ch_y in diffs)

for row in range(6):
  for col in range(6):      
    if grid[row][col] == '0' and adjacent_sum(col, row) == 3:
      endrow, endcol = row, col
    elif grid[row][col] == '#':
      startrow, startcol = row, col

grid[startrow][startcol] = "0"
grid[endrow][endcol] = "#"

for row in grid:
    print("".join(row))

# ALSO CONSIDER
'''

from itertools import product

grid = [list(input()) for _ in range(6)]
deltas = ((0,1),(0,-1),(1,0),(-1,0))

for x,y in product(range(6),range(6)):
  if grid[y][x] == "#":
    break

grid[y][x] = "0"
visited = set()
stack = [(x,y)]

while stack:
  current = stack.pop()
  visited.add(current)
  for d in deltas:
    x,y = (current[0]+d[0])%6, (current[1]+d[1])%6
    if (x,y) not in visited and grid[y][x] == "0":
      stack.append((x,y))

x,y = current
grid[y][x] = "#"
for row in grid:
  print("".join(row))

'''
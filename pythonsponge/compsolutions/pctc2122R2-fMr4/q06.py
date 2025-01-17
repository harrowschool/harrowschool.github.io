width, height = int(input()), int(input())
data = [list(map(int, input())) for _ in range(height)]

subgrid_size_x = width // 2
subgrid_size_y = height // 2

grid_starts = ((0,0), (subgrid_size_x,0), (0,subgrid_size_y), (subgrid_size_x,subgrid_size_y))

total = 0

for y in range(subgrid_size_y):
    for x in range(subgrid_size_x):
        visible = 1
        for a,b in grid_starts:
            visible *= data[b+y][a+x]
        total += visible

print(total)
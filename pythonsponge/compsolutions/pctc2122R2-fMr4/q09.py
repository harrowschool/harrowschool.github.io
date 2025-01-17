from itertools import product

def get_grid():
    grid = [list(map(int, input())) for _ in range(10)]
    a, b = min((a,b) for a,b in product(range(10), range(10)) if grid[b][a] == 1)
    return set((a-c,b-d) for c,d in product(range(10), range(10)) if grid[d][c] == 1)

first = get_grid()
print(sum(get_grid() == first for _ in range(5)) * len(first))
n = int(input())

rows = list(range(0,10))
cols = list(range(0,10))

for _ in range(n):
    order = input()
    if order[0] == 'r':
        rows = rows[:int(order[1])] + rows[int(order[3])+1:]
    else:
        cols = cols[:int(order[1])] + cols[int(order[3])+1:]

for row in rows:
    print(" ".join([f"{row}{col}" for col in cols]))
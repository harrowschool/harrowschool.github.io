total = 0
count = 0

while total != 20:
    total += int(input())
    count += 1
    if total > 20:
        total = 0

print(count)

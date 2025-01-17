size = int(input())
inner = int(input())
ch1 = input()
ch2 = input()

spacelines = ((size - inner) - 2) // 2

print(ch1 * size)

for _ in range(spacelines):
    print(ch1 + " " * (size - 2) + ch1)

for _ in range(inner):
    print(f"{ch1}{ch2 * inner:^{size-2}}{ch1}")

for _ in range(spacelines):
    print(ch1 + " " * (size - 2) + ch1)

print(ch1 * size)
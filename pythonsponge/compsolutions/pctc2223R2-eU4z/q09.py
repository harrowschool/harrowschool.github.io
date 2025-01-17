import math

n = int(input())

bestlx, bestly = 0, 0
besthx, besthy = math.inf, math.inf

for _ in range(n):
    lx, ly, w, h = map(int, input().split())
    bestlx = max(bestlx, lx)
    bestly = max(bestly, ly)
    besthx = min(besthx, lx + w)
    besthy = min(besthy, ly + h)

print((besthy - bestly) * (besthx - bestlx))
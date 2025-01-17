x, t, y = (int(input()) for _ in range(3))

lead = x * t
reduces = lead // (y - x)
hops = t + reduces

if lead % (y - x) != 0:
    hops += 1

print(hops)
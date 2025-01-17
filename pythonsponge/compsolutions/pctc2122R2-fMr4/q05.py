q1, q2 = int(input()), int(input())

small = min(q1, q2)
big = max(q1, q2)

if q1 > 20 or q2 > 20:
    # only one scenario
    print(f"£{small}.{big:}")
else:
    print(f"£{small}.{big:02}")
    print(f"£{big}.{small:02}")
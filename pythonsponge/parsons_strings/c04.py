nums = []
for count in range(3):
    nums.append(float(input("next number? ")))
print("|  NUMBER  |  SQUARE  |")
print("+----------+----------+")
for num in nums:
    print(f"|{num:^10.2f}|{num**2:^10.2f}|")

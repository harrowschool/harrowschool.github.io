num1 = int(input())
num2 = int(input())
num3 = int(input())

result = num1 ** 2 + num2 ** 2

if result < num3 ** 2:
  phrase = "less than"
elif result > num3 ** 2:
  phrase = "greater than"
else:
  phrase = "equal to"

print(f"{num1} squared plus {num2} squared is {phrase} {num3} squared")

'''
# ALSO OF INTEREST...

a, b, c = [int(input()) for _ in range(3)]

cmp = lambda a,b: (a > b) - (a < b)
phrases = ["less than", "equal to", "greater than"]
result = cmp(a**2 + b**2, c**2) + 1

print(f"{a} squared plus {b} squared is {phrases[result]} {c} squared")


'''
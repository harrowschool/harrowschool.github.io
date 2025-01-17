# extension: can you find a neater way to do this e.g. using a list?

num1 = int(input())
num2 = int(input())
num3 = int(input())

if num1 >= num2 and num1 >= num3:
  if num2 <= num3:
    print(num3)
  else:
    print(num2)
elif num2 >= num1 and num2 >= num3:
  if num1 <= num3:
    print(num3)
  else:
    print(num1)
else:
  if num1 <= num2:
    print(num2)
  else:
    print(num1)
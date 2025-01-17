x = int(input())
y = int(input())

if x > y:
  print(x - y)
else:
  print(y - x)

# also consider

'''
x, y = int(input()), int(input())
print(max(x-y, y-x))
'''
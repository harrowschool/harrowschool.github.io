a = int(input())
b = int(input())
c = int(input())

if a <= b and a <= c:
  side = a
elif b <= a and b <= c:
  side = b
else:
  side = c
  
# or students might know to use:
# side = min(a, b, c)
  
perimeter = 4 * side
area = side ** 2

print(side)
print(perimeter)
print(area)

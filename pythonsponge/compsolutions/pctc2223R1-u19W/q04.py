n1 = int(input())
n2 = int(input())

dist = 100 - (n1 + n2)
if dist < 0:
  dist *= -1

min_dist = dist

dist = 100 - (n1 - n2)
if dist < 0:
  dist *= -1
if dist < min_dist:
  min_dist = dist
  
dist = 100 - (n2 - n1)
if dist < 0:
  dist *= -1
if dist < min_dist:
  min_dist = dist
  
print(min_dist)

# or consider using

'''
def score(x):
  return abs(x - 100)

a = int(input())
b = int(input())

tests = [a-b, b-a, a+b]
print(min(score(v) for v in tests))
'''
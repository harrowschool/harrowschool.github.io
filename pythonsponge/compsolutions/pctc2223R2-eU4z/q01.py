a,b,c = int(input()), int(input()), int(input())

if a <= b <= c:
  first, last, diff = a, c, b - a
elif a <= c <= b:
  first, last, diff = a, b, c - a
elif b <= a <= c:
  first, last, diff = b, c, a - b
elif b <= c <= a:
  first, last, diff = b, a, c - b
elif c <= a <= b:
  first, last, diff = c, b, a - c
else:
  first, last, diff = c, a, b - c
  
print(first - diff)
print(last + diff)

# ALSO CONSIDER

'''
nums = sorted(int(input()) for _ in range(3))
diff = nums[1] - nums[0]
print(nums[0] - diff)
print(nums[2] + diff)
'''
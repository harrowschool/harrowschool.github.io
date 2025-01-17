code = int(input())
key = int(input())
 
for count in range(key):
  code = code * 2 + 1
 
print(code)

'''
# ALSO OF INTEREST...

from functools import reduce
code, key = int(input()), int(input())
print(reduce(lambda x, y: 2 * x + 1, range(key), code))

'''
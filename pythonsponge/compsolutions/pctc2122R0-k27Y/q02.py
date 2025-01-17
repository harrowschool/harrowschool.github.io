pay = int(input())
change = int(input())
 
if change > 0:
  print(pay + change)
else:
  print(pay)

'''
# ALSO OF INTEREST...

pay, change = int(input()), int(input())
print(pay + change if change > 0 else pay)

'''
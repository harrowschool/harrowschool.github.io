hats = int(input())
scarves = int(input())
gloves = int(input())

count = 0
used = 0

if hats >= 1:
  count += 1
  used += 1
  
if scarves >= 1:
  count += 1
  used += 1
  
if gloves >= 2:
  count += 1
  used += 2
elif gloves == 1:
  used += 1
  
if count >= 2:
  print("toasty")
else:
  print("cold")
  
print(hats + scarves + gloves - used)
  
apples, oranges = 50, 50

while apples > 0 and oranges > 0:
  
  fruit = input()
  quantity = int(input())
  
  if fruit == "APPLES":
    apples = max(0, apples - quantity)
  else:
    oranges = max(0, oranges - quantity)
      
print(apples + oranges)
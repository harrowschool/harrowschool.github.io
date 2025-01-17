pay = int(input())
sales = int(input())

if sales > 10:
  pay += 60
elif sales > 8:
  pay +=5
elif sales > 5:
  pay += 20
  
print(pay)
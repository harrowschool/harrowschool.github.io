length = 1
delta = int(input())
days = int(input())

for day in range(days):
  print('o' * length + '{')
  length += delta

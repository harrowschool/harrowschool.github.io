size = int(input("enter an odd number for the first row: "))

for row_length in range(size, 0, -2):
  row = "_" * row_length
  print(f"{___:^{____}}")
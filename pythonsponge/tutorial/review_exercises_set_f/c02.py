HEADER = "+----------+----------+"
LAYOUT = "|{0:^10}|{1:^10}|"

furniture = ["table", "chair", "bookcase", "cabinet"]
weights = [18.8, 8.2, 14.3, 32.1]

min_weight = float(input("enter a min weight to filter: "))

print(HEADER)
print(LAYOUT.format("ITEM", "WEIGHT"))
print(HEADER)

for count in range(len(_________)):
  if weights[count] >= __________:
	print(LAYOUT.format(furniture[count], ______________))
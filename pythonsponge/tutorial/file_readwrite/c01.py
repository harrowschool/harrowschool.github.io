file = open("data.txt", "w")

print("enter the name of three friends...")

prefix = "" # don't write a new line before the first line
for idx in range(3):
  file.write(prefix + input('enter your next name: '))
  prefix = "\n"

file.close()
print("all done...now proceed to the next exercise where we will load your data back...")
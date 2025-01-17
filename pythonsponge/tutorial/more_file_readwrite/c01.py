names = []

prefix = ""
for count in range(3):
  names.append(prefix + input("enter name: "))
  prefix = "\n"

file = open("data.txt", "w")
file.writelines(names)
file.close()

file = open("data.txt", "r")
contents = file.readlines()
file.close()

print("These names have been saved to a file:")
for line in contents:
  print(line.strip())
# not a great data format but sometimes we have to deal with it!
results = ["Jasmine", 37, "Mark", 26, "Antoin", 51, "Emily", 47]
LINE_LAYOUT = "{0}{1},{2}"

prefix = ""
file = open("pythag.txt", "w")
for idx in range(0, len(results), 2):
  line = LINE_LAYOUT.format(prefix, results[idx], results[idx+1])
  file.write(line)
  prefix = "\n"
file.close()

# Now add one more name and score
name = input("new name: ")
score = int(input("new score: "))

file = open("pythag.txt", "a")
line = LINE_LAYOUT.format(prefix, name, score)
file.write(line)
file.close()

# Let's check they are all here:
file = open("pythag.txt", "r")
for line in file:
  print(line.strip())
file.close()
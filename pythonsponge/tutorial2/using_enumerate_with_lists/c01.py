word = "CAT"
for i in range(0, len(word), 1):
  print("At position", i, "the character is", word[i])
	
print("nicer code...")

for i, ch in enumerate(word):
  print("At position", i, "the character is", ch)

word = input("enter a single word with several characters: ")

print("chop chop chop...")

while len(word) > 0:
  word = word[1:]
  print(word)
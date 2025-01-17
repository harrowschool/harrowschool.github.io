word = input("enter a word: ")
phrase = input("enter a phrase: ")
if word in phrase:
  print("yes I can find", word, "in that phrase")
else:
  print("no I can't find", word, "in that phrase")
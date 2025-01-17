word = input("enter a word: ")
letter = input("enter a letter to find in your word: ")

pos = word.find(letter)

if pos == -1:
  print("you didn't use that letter!")
else:
  print("you first used", letter, "at index", pos)
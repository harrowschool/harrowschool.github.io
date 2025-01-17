word = input("enter a word: ")

letters = list(word)
letters.sort()

print("the letters you used, in alphabetical order, are")
print(",".join(letters))

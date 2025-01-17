def extend_word(word, stem):
  return word + stem

word1 = input("enter root word e.g. jump: ")	
print(extend_word(word1, "ed"))

word2 = input("enter root word e.g. walk: ")
print(extend_word(word2))
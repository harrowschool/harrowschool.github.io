word = input("enter a sentence containing and at least twice: ").lower()
MATCH = "and"

find1 = word.f___(MATCH)

# replace the word only the FIRST time it occurs
word = word.replace(MATCH, "---", 1) 

find2 = word.f___(_____)
print("the second time and occurs is at index", find2)
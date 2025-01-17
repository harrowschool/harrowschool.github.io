liked_words = []
for count in range(5):
    word = input("next word: ").lower()
    if word[0] == "p" and word[-1] in "aeiou":
        liked_words.append(word)
print(liked_words)
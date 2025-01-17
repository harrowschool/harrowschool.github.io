def score_word():
    ''' This function calculates the score of a word based on the number of vowels in the word. '''
    global score
    for letter in word:
        if letter.lower() in "aeiou":
            score += 1

word = input("enter your word to score: ")
score = 0
score_word()
print("your score is", score)

# WORD GUESS

# GET THE CHALLENGE WORD
while True:
  inputtedWord = input('Player 1 choose your game word please: ').lower()  #.lower() turns inputtedWord all lowercase
  if inputtedWord.isalpha() and " " not in inputtedWord:
    break
  else:
    print("THAT ISN'T A WORD!")

foundLetters = "_" * len(inputtedWord)
lives = 5 
GameWon = False

print("\n" * 50 + f'WELCOME TO WORD GUESS\n YOU HAVE {lives} LIVES')
print("CURRENT STATE:", foundLetters)

while not GameWon and lives > 0:

  # GET THE NEXT CHALLENGE LETTER
  while True:
    # TASK 1 ==> ADD A FUNCTION CALL TO THIS NEXT LINE (ALREADY USED IN THIS PROGRAM ABOVE) TO TURN THIS INPUT INTO LOWERCASE
    guess = input('Player 2, please guess your next letter: ')

    # TASK 2 ==> CHANGE THE True below TO USE TWO CHECKS INCLUDING A FUNCTION (ALREADY USED IN THIS PROGRAM ABOVE) SO THAT IT ONLY BREAKS IF THEY ENTER A SINGLE LETTER
    if True:
        break
    else: 
        print("That's not a letter!")

  for i in range(len(inputtedWord)):
    if inputtedWord[i] == guess:
      foundLetters = foundLetters[:i] + guess + foundLetters[i+1:]

  if guess in inputtedWord:
    print(f'CORRECT! {foundLetters} \n')
  else:
    lives -= 1
    #TASK 3 ==> PRINT OUT USING THE 'f string' FORMAT SEEN ABOVE, A MESSAGE TO STATE THE NUMBER OF LIVES LEFT
  
  if '_' not in foundLetters:
    GameWon = True

if GameWon==False:
  print('YOU HAVE NO LIVES LEFT!\nGAME OVER!')
else:
  # TASK 4 ==> FIGURE OUT WHAT CODE MAKES SENSE TO BE WRITTEN HERE
  pass  



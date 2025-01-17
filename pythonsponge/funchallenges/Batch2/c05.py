import random

ROUNDS = 3
playerNumber = 3
BankAccounts = [0.0, 0.0, 0.0]
RandomPrizes = [75, 100, 125]
StealPercentages = [10, 25, 50]
players = []

# ==> Task 1: find a way to add one or more questions of your own to the game
questions = {
  'Who invented the turing machine? A) Alan Turing, B) Mac Turing, C) Mr Baker, D) Frank Turing': "A", 
  "Which of these languages was used by NASA in early space exploration? A) Python, B) Fortran, C) Java, D) HTML":"B",
  "What is the capital of Belgium? A) Lindor, B) Toberlorone, C) Legumes, D) Brussels":"D",
  "Who was the first person in space? A) Yuri Gagarin, B) Neil Armstrong, C) Lance Armstrong, D) Bruce Moon":"A", 
  "How long is an olympic swimming pool? A) 25m ,B) 75m, C) 80ft D)50m":"D"
}

# input player names
for i in range(playerNumber):
  playername = input(f'Player {i+1} what should we call you? ')
  players.append(playername.upper())

#this game loop will repeat the following code once for each of the rounds
for i in range(ROUNDS): 
  print(f'Round {i+1} of {ROUNDS}: current prize-pots for {", ".join(players)} are respectively:')
  print(BankAccounts)

  for indexofPlayer, currPlayer in enumerate(players): #in every round we will ask each player a question  
    randomQuestion = random.choice(list(questions.keys()))
    print(f"It is now {currPlayer}'s turn")
    print(randomQuestion)
    userAnswer = input('choose a, b, c or d? ')

    if userAnswer.upper() == questions[randomQuestion]:
      # ==> Task 2: change these next two lines
      # ==> to randomise the prize and steal percentage awarded each time 
      # ==> Hint: you will want to use the random library!
      PrizeAward = RandomPrizes[1] 
      StealPercent = StealPercentages[1]

      BankAccounts[indexofPlayer] += PrizeAward
      print(f'That\'s right!!! You gained £{PrizeAward}, your total is now {BankAccounts[indexofPlayer]}')
      print(f"You may now steal {StealPercent}% from a fellow competitor")
      
      victim = None
      while victim not in players:
          print(f'Who, out of {", ".join(players)} would you like to steal from?')
          print(f'Their respective bank account values are {BankAccounts}')
          victim = input().upper()

      indexOfVictim = players.index(victim)
      StealAmount = round(BankAccounts[indexOfVictim] * StealPercent / 100, 2)
      BankAccounts[indexofPlayer] += StealAmount
      BankAccounts[indexOfVictim] -= StealAmount

      BankAccounts[indexofPlayer] = round(BankAccounts[indexofPlayer], 2)
      BankAccounts[indexOfVictim] = round(BankAccounts[indexOfVictim], 2)

      print(f'You have stolen £{StealAmount} from {victim} and now have a bank balance of £{BankAccounts[indexofPlayer]}')
      input('Press enter to continue...')

    else:
      # ==> Task 3: An output belongs here
      # ==> remove the word pass on the next line 
      # ==> instead figure out what the output should be and add it to the code.
      pass 
        
    # ==> Task 4: modify the code above to allow the player to choose not to steal in return for an extra 25 points
    # ==> Task 5: create another rule/feature of your own to add to this game

    # scrolling the page down to hide previous answers
    print('\n' * 100)
   
winner = players[BankAccounts.index(max(BankAccounts))]
print(f'Final bank accounts for {", ".join(players)} are respectively:')
print(BankAccounts)
print(f'{winner} IS VICTORIOUS!')
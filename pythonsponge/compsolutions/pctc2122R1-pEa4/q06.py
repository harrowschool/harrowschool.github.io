word1 = input()
word2 = input()

if word1 == "rock" and word2 == "scissors":
  print("5-0")
elif word1 == "scissors" and word2 == "rock":
  print("0-5")
elif word1 == "scissors" and word2 == "paper":
  print("5-0")
elif word1 == "paper" and word2 == "scissors":
  print("0-5")
elif word1 == "paper" and word2 == "rock":
  print("5-0")
elif word1 == "rock" and word2 == "paper":
  print("0-5")
else:
  score1 = int(input()) + 1
  score2 = int(input()) + 1
  print(f"{score1}-{score2}")

def getAllIndexes(arr, val):
  indexes = []
  for idx in range(len(arr)):
    if arr[idx] == val:
      indexes.append(idx)
  return indexes

while True:
  code = input("Player A: Enter a 4 digit code using only letters A-F (duplicates are allowed): ").upper()
  # TASK 4 ==> Can you make the code only accept the letters A-F?
  if len(code) == 4:
    break
  print("invalid code...")

# TASK 1 ==> Can you add print statement(s) so that player 2 doesn't see the code player 1 entered?

for attempt_number in range(9):
 
  print(f"[Attempt {attempt_number+1} out of 9]")

  attempt = input(f"Player B: guess the code: ").upper()

  if attempt == code:
    print()
    # TASK 2 ==> Can you make the number of attempts print out correctly - it is out by one!
    print(f"Congratulations! Player B guessed the code in {attempt_number} attempt(s)!")
    # TASK 3 ==> Can you make this next line print out correctly as well?
    print("Player A gets {attempt_number} point(s), Player B gets {9 - attempt_number} point(s)")
    break
 
  verifiedIdxs = []
  num_right_place = 0
  num_wrong_place = 0

  for idx in range(len(attempt)):
    if attempt[idx] == code[idx]:
      num_right_place += 1
      verifiedIdxs.append(idx)

  for idx in range(len(attempt)):
    if attempt[idx] != code[idx]:
        idxs = getAllIndexes(code, attempt[idx])
        for i in idxs:
            if i not in verifiedIdxs:
                num_wrong_place += 1
                verifiedIdxs.append(i)
                break

  print(f"HINT: {num_right_place} letter(s) are correct and in the right place")
  print(f"HINT: {num_wrong_place} letter(s) are correct but in the wrong place\n")

# TASK 5 ==> If they get the code on the last attempt it still says they failed to guess the code - can you fix that?
if attempt_number == 8:
  print(f"Player B failed to guess the code. The code was {code}")
  print("Player A gets 9 points, Player B gets 0 points")
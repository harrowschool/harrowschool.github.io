CODE="""
output = None
returnLine = -1
hand = []

goto(36) # goto the start of the main code

# gets the value input from the user

card = input("Enter Your Card Number (2-10,A,J,Q,K): ")
cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
if card in cards:
  output = card
  goto(returnLine)

print("Invalid Input")
goto(8)

# gets the suit input from the user

suit = input("Enter Your Suit: ")
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
if suit in suits:
  output = suit
  goto(returnLine)

print("Invalid Input")
goto(19)

# prints the hand
output = None
print("; ".join([f"{i[1]} of {i[0]}" for i in hand]))
print("Total Value:", sum([int(i[1]) if i[1].isdigit() else (11 if i[1] == "A" else 10) for i in hand]))
goto(returnLine)

# Start of the main code

# Get two cards from the user
returnLine = XXX # we want to return below the goto call
goto(XXX) # card value function call
value = output
returnLine = XXX # we want to return below the goto call
goto(XXX) # card suit function call
hand.append((output, value))

if len(hand) < 2:
  print("Enter second card")
  goto(XXX) # goto for looping

# print the hand
returnLine = XXX # we want to return below the goto call
goto(XXX) # print hand function call

"""

# Do Not Edit beyond this point

####################################################################################
# Complex function to recursively goto (continue execution from) a line number
def goto(L):
  try:C=list(map(lambda x:'raise Exception("Use of for or while is not allowed this week!")\nif 0:'if __import__("re").search(r'^\s*(for|while|def)',x)else x.replace('goto(stop)','raise SystemExit'),CODE.split("\n")));exec("\n".join(C[(L-1):]),globals())
  except IndentationError:L+=[any([not i.isspace()for i in C[(K-1)]])for K in range(L,len(C))].index(True);N=C[(L-1):];Y=N[0][:[1if not i.isspace()else 0for i in list(N[0])].index(1)];N=[i.removeprefix(Y)for i in N];exec("\n".join(N),globals())
  except Exception as e:raise e
####################################################################################

####################################################################################
# Main call
__import__("sys").setrecursionlimit(500) # 500 chosen as it allows max depth before pydide crashes
try:
  CODE += "\ngoto(stop)" # in case the user forgets this line
  goto(1) # initiate the program at line one
except RecursionError as e:
  raise Exception("Infinite Loop Reached! GoTo was caught in an infinite loop!") 
  # recursion error occurs when the user's code has one goto chain longer than 164
except SystemExit as e:
  pass # success
except Exception as e:
  raise e # an error in the user's code
####################################################################################
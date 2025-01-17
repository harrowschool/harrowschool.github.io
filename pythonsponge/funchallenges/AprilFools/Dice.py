CODE="""

dice1 = 1
dice2 = 1

# Start of goto loop
if dice1 == 6: # reset dice1 to 1 and change dice2
  dice1 = XXX
  dice2 += XXX

dice1 += 1

if dice2 > 6: # we are now done!
  goto(stop)

print(f"Dice Rolled {dice1}, {dice2} Sum to: {dice1 + dice2}")

goto(XXX) # goto for looping


"""

# Do Not Edit beyond this point

####################################################################################
# Complex function to recursively goto (continue execution from) a line number
def goto(L):
  try:C=list(map(lambda x:'raise Exception("Use of for or while is not allowed this week!")\nif 0:'if __import__("re").search(r'^\s*(for|while)',x)else x.replace('goto(stop)','raise SystemExit'),CODE.split("\n")));exec("\n".join(C[(L-1):]),globals())
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
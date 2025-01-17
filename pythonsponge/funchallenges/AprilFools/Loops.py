CODE="""
count = 10
# Replaces 'for count in range(10, 0, -1):'

if count == 0:
  goto(13)

print(count)
count -= 1

goto(4) # Goes back up to line 4. This is used for looping!


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
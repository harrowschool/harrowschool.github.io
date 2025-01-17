valid = False
while valid == False:
  code = input("enter the employee 3-letter uppercase code: ")
  if len(code) == 3 and code.isalpha() and code.isupper():
    valid = True
  else:
    print("error, please try again...")

print("code accepted")

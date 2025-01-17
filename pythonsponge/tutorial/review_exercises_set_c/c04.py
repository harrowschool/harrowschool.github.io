valid = False
while not valid:
  code = input("enter the two digit code in the format Aa (e.g. Nd): ")
  if code.isalpha() and len(code) == 2 and code[0].isupper() and _________________:
    valid = ____
  else:
    print("try again...")
print("accepted")
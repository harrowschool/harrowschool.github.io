digits = "0123456789"
 
while True:
  code = input()
  if len(code) == 5:
    starter = code[0] + code[1]
    if starter == "TH":
      if code[2] in digits and code[3] in digits and code[4] in digits:
        break
        
print(code)

'''
# ALSO OF INTEREST...

while len(code := input()) != 5 \
      or code[:2] != "TH" \
      or not code[2:].isdigit():
  pass
print(code)


'''
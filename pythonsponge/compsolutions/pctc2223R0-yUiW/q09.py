code = [""] * 5

for i in range(5):
  inp = input()
  loc = int(inp[0]) - 1
  code[loc] = inp[1]
  
print(code[0]+code[1]+code[2]+code[3]+code[4])

'''
# ALSO OF INTEREST

code = "_____"

for i in range(5):
  inp = input()
  loc = int(inp[0]) - 1
  code = code[:loc] + inp[1] + code[loc+1:]
  
print(code)

'''

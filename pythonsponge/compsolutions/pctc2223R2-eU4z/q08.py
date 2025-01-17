cipher = input()
stack = []

for char in cipher:
    if char == "[":
        stack.append([])
    elif char.isdigit():
        stack[-1].append(int(char))
    elif char == "]":
        temp = stack.pop()
        print((temp[0] + temp[-1]) // 2, end="")

print()

# ALSO CONSIDER

'''

def showcode(data):
  l = len(data)
  i = 0
  while i < l:
    if isinstance(data[i],list):
      showcode(data[i])
      del data[i]
      l -= 1
    else:
      i += 1
  print((data[0]+data[-1])//2, end="")

showcode(eval(input()))
print()

'''
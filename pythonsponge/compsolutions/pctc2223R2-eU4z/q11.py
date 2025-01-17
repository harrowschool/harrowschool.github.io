limit = str(int(input()) + 1)[::-1]

total = 0

for pos in range(len(limit)):
    digit = int(limit[pos])
    prefix = limit[pos+1:].count('7')
    total += digit * pos * (10 ** max(pos-1, 0)) + prefix * digit * (10 ** pos)
    if digit > 7:
        total += 10 ** pos

print(total)

# ALSO CONSIDER RECURSIVE

'''
store = {}

def sevens(n):
  if n in store:
    return store[n]
  elif len(n) == 1:
    return (1 if int(n) >= 7 else 0)

  result = sevens("9" * (len(n)-1)) * int(n[0])
  result += sevens(n[1:])

  if n[0] == "7":
    result += int(n[1:]) + 1
  elif n[0] in "89":
    result += 10 ** (len(n)-1)

  store[n] = result
  return result

# keep input as string
upto = input()
print(sevens(upto))

'''
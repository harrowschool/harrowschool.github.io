# extension: could you find a neater way to achieve this without the long inner if?

message = input()
cipher = ""

for ch in message:
  if ch in "AEIOU":
    if ch == "A":
      cipher += "E"
    elif ch == "E":
      cipher += "I"
    elif ch == "I":
      cipher += "O"
    elif ch == "O":
      cipher += "U"
    elif ch == "U":
      cipher += "A"
  elif ch != " ":
    cipher += ch
    
print(cipher)
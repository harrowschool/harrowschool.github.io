# extension: can you find a neater way to do this using a loop?

pin = input()

if int(pin[1]) <= int(pin[0]):
  print(int(pin[1]))

if int(pin[2]) <= int(pin[1]):
  print(int(pin[2])) 

if int(pin[3]) <= int(pin[2]):
  print(int(pin[3]))
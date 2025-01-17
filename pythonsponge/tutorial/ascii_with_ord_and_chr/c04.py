def encoder(char, rotateBy):
  encoded = ___(char.upper()) + rotateBy
  if encoded > ord('Z'):
    encoded -= 26
  return chr(_______)
	
rotateChoice = int(input("rotate right by how many characters 1-25? "))

for char in input("enter message: ").replace(" ", ""):
  print(encoder(____, ____________), end="")
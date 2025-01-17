char = input("enter a single character to encode: ").upper()
encoded = ord(char) + 1
if encoded > ord('Z'):
  encoded -= 26
cipherLetter = chr(encoded)
print("your encoded character is:", cipherLetter)
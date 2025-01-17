cipherText = "olssv dvysk!"
alphabet = "abcdefghijklmnopqrstuvwxyz"

for key in range(1, 26):

  plainText = ""

  # For each possible encryption key, decrypt the cipher text and print it with the key 
  for character in range(len(cipherText)):

    if cipherText[character] not in alphabet:
      # If the character is not a letter, add it to the plain text
      # HINT: look at line 8 for a clue for the blank
      plainText += cipherText[______]
    else:
      characterIndex = alphabet.index(cipherText[character])
      # Shift the character
      # The '% 26' prevents errors occuring when wrapping around the alphabet from z->a
      # HINT: For this blank, you will need the variable that changes each loop
      newCharacterIndex = (characterIndex + _____) % 26 
      # Add the new character to the plain text
      # 
      plainText += alphabet[_________]
	  
  # Replace the underscores with the correct variable names
  print(f"Key: {key} | Plain Text: '{plainText}'")

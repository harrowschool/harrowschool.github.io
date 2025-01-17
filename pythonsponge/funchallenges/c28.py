# Caesar cipher encryption
ALPHABET = "abcdefghijklmnopqrstuvwxyz"

def ceasar_shift(msg, shift):

  cipher_text = ""

  # remove all spaces, they are a dead give away!
  msg = msg.replace(" ", "")

  # make sure it is all lower-case
  msg = msg.lower()

  # loop through every character in the message
  for character in msg:

    # only process it if it is a letter from the alphabet
    if character in ALPHABET:
      
      # find its new position including wrap-around if needed using the mod operator %
      # TASK ==> FIX THE BUG BELOW SO THAT IT SHIFTS BY THE REQUESTED NUMBER OF LETTERS
      position = ALPHABET.index(character)
      new_position = (position + 1) % len(ALPHABET)

      # add the new character to the encoded text
      cipher_text += ALPHABET[new_position]

  return cipher_text

def ceasar_decode(msg):
  print("PERHAPS IT WAS THIS?")
  # TASK ==> ADD A LOOP BELOW SO THAT IT PRINTS EACH OF THE POSSIBLE SHIFT OUTPUTS NOT JUST ONE OF THEM
  # try one of the possible shifts
  print(ceasar_shift(msg, 5))

choice = input("ENTER 1 to ENCODE or 2 TO DECODE: ")

match choice:

  case "1":
    message = input("Enter message to encode e.g. Flee! All has been discovered: ")
    change = int(input("How many characters would you like to Ceasar shift by? "))
    print("ENCODED MESSAGE:", ceasar_shift(message, change))

  case "2":
    cipher = input("What message would you like to decode? ")
    ceasar_decode(cipher)

  case other:
    print("invalid option")

morse_code = {
'A':'.-', 'B':'-...',
'C':'-.-.', 'D':'??', 'E':'.',
'F':'..-.', 'G':'--.', 'H':'....',
'I':'..', 'J':'.---', 'K':'-.-',
'L':'??', 'M':'--', 'N':'-.',
'O':'---', 'P':'??', 'Q':'--.-',
'R':'.-.', 'S':'...', 'T':'-',
'U':'..-', 'V':'...-', 'W':'.--',
'X':'-..-', 'Y':'-.--', 'Z':'--..',
'1':'.----', '2':'..---', '3':'...--',
'4':'....-', '5':'.....', '6':'-....',
'7':'--...', '8':'---..', '9':'----.',
'0':'-----', ', ':'--..--', '.':'.-.-.-', ' ':' '
}

# MORSE CODE ENCODER
def encoder():
  # TASK 2: add a line below to ask the user to input a sentence
  sentence = _____

  # TASK 3: complete the for loop
  for char __ ________:
    print(__________, end = " ")
    

# MORSE CODE DECODER
def decoder():
  # TASK 5: take another input from the user.

  # here we split the sentence into words using .split()
  sentence = sentence.split("   ")
  morse_code_reverse = {val:key for key, val in morse_code.items()}
	
  # TASK 6: loop through each word in the sentence (by removing the triple quotes)
  '''  
  ___ word __ _______:
    message = "".join(morse_code_reverse[code] for code in word.split(" "))
    print(message)
  '''

choice = input(("Enter e to encode a message and d to decode a message: "))
if choice == "e":
  encoder()
# TASK 7: call the decoder function


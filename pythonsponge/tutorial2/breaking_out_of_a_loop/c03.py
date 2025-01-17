sentence = ""
while True:
  word = input("enter the next word for the sentence: ")
  sentence += word
  if len(sentence) > 30:
    sentence += "."
    break
  sentence += " "
print("your final sentence is...")
print(sentence)
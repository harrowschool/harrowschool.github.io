story = ""

while True:
  word = input()
  if word == "stop":
    break  
  if len(story) > 0:
    story += " "
  story += word
  
print(story)

'''
# ALSO OF INTEREST

story = ""
while (word:=input()) != "stop":
  story += f"{word} "
print(story[:-1])

'''

'''
# ALSO OF INTEREST

def get_words():
  while (word:=input()) != "stop":
    yield word
    
print(" ".join(w for w in get_words()))

'''


subject = input("enter your favourite school subject: ")

MESSAGE1 = "you entered {0} which has {1} characters in it"
MESSAGE2 = "can you find a subject with {0} characters?"

print(MESSAGE1.format(subject, len(subject)))
print(MESSAGE2.format(len(subject) + 1))
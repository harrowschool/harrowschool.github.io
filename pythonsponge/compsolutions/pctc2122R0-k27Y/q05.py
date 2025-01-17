word = input()
firstletter = word[0]
lastletter = word[-1]
 
print(lastletter + word[1:-1] + firstletter)

'''
# ALSO OF INTEREST...

print((word := input())[-1] + word[1:-1] + word[0])

'''
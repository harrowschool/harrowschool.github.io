chr1 = 'A'
chr2 = 'a'
chr3 = '&'

print(chr1, "has code", ord(chr1))
print(chr2, "has code", ord(chr2))
print(chr3, "has code", ord(chr3))

nextCode = ord(chr1) + 1
nextCharacter = chr(nextCode)
print(nextCharacter, "is next in ASCII after", chr1)
from random import randint

testdata = ""


while len(testdata) < 1000:
    testdata += chr(ord("A") + randint(0, 25))

print(testdata)

def makeName(name):
    print("Dear", name)
def makeVerse(phrase, name, numberOfDears, terminator):
    print(phrase)
    for i in range(numberOfDears):
        makeName(name)
    print(phrase)
    for i in range(numberOfDears - 1):
        makeName(name)
    print(terminator)
makeVerse("There's a hole in my bucket", "Liza", 2, "a hole")
makeVerse("Then mend it", "Henry", 3, "mend it")
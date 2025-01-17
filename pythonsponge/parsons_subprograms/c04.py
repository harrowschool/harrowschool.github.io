def doHorizontal():
    print("-----")
def doLetterI():
    doHorizontal()
    for _ in range(4):
        print(f"{'|':^5}")
    doHorizontal()    
doLetterI()
doLetterI()
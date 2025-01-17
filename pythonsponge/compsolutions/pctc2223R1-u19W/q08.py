word = input()
original = word

def do_peel(word):
    middle = len(word) // 2
    first = word[:middle]
    second = word[middle:]
    return first[-1] + first[:-1] + second[1:] + second[0]


while True:
    word = do_peel(word)
    print(word)
    if word == original:
        break

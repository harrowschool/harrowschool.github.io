def get_character(string, position):
    return string[position]


def remove_letters(string, letters):
    for letter in letters:
        string = string.replace(letter, "")
    return string


line = "In fair Verona where we lay our scene"
positions = [3, 4, 6, 7, 13, 15, 25, 26]

characters = map(lambda position: get_character(line, position), positions)
print("".join(characters))

words = map(lambda word: remove_letters(word, "ae"), line.split(" "))
print(list(words))

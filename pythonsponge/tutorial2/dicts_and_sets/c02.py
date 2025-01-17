# Checking if a letter is a vowel
string = "height and area"
vowels = ["a", "e", "i", "o", "u"]
for letter in string:
    if letter in vowels:
        print(f"{letter} is a vowel")
    else:
        print(f"{letter} is not a vowel")

# Tracking a bookshop's inventory of unique items
books = ["The Lord of the Rings", "Moby Dick", "Crime and Punishment"]
# Acquired some more books
books.append("Nicholas Nickleby")
books.append("Jane Eyre")
# Check if a book is in stock
if "Of Mice and Men" in books:
    print("We have that book in stock")
else:
    print("We don't have that book in stock")
# Some books have been sold
books.remove("The Lord of the Rings")

# Replacing letters in a string
string = "In Hertford, Hereford, and Hampstead, hurricanes hardly ever happen"
replaced = []
for char in string:
    if char == "H" or char == "h":
        replaced.append("'")
    else:
        replaced.append(char)
print("".join(replaced))

# Combining collections
squares = [4, 9, 64, 256]
cubes = [8, 27, 64, 512]
all_powers = squares + cubes
# Numbers are sixth powers if they are both squares and cubes. The list comprehension below can be replaced with a
# simple set operation.
sixth_powers = [n for n in squares if n in cubes]
for num in range(513):
    if num in all_powers:
        print(f"{num} is a power of another number")
    if num in sixth_powers:
        print(f"{num} is a sixth power of another number")

# List and string indexing
words = ["two", "households", "both", "alike", "in", "dignity"]

# You can get an element of a list or a letter of a string by putting the index in square brackets as below
# Pitfall: indexes are out by one. [0] actually gets the first element! Then [1] gets the second element and so on
print("first word:", words[0])
print("first letter:", words[0][0])
print("second letter:", words[0][1])

# DON'T CHANGE ME
___ = 1

print("NOW COMPLETE THE GAPS BELOW TO GET THE PROGRAM TO RUN CORRECTLY AND GIVE YOU ALL OF YOUR POINTS!")

# TASK 1: Get the "k" of "alike" by replacing the ___ below
answer = words[___][___]
print(answer)
assert answer == "k", "Complete task 1 correctly to get past this point"
print("YAAY, FIRST POINT SCORED!")


# You can also get from the end of the list by using negative indexes
# [-1] gets the last element, [-2] the second-last, and so on
print("last word:", words[-1])
print("last letter:", words[-1][-1])
print("penultimate letter:", words[-1][-2])

# TASK 2: Get the "n" of "in", using negative indices
answer = words[___][___]
print(answer)
assert answer == "n", "Complete task 2 correctly to get past this point"
print("HOORAH, SECOND POINT SCORED!")


# You can get slices of the list, rather than individual elements, using colons
# [a:b] gets all the elements between index a and index b
# Pitfall: this is INCLUSIVE of a but EXCLUSIVE of b!

print("first three words:", words[0:3])
print("extracting bot:", words[2][1:3])

# You can also omit the number before the colon to slice from the start of the sequence,
# and/or the number after the colon to slice up to the end
print("extracting like:", words[3][1:])


# TASK 3: Get the word "dig" from "dignity"
answer = words[___][___:___]
print(answer)
assert answer == "dig", "Complete task 3 correctly to get past this point"
print("WOWZAH, THIRD POINT SCORED!")


# You can also specify a "step", to get elements at regular intervals, by including a second colon
# [a:b:2] gets every other element between a and b (again inclusive of a but exclusive of b)
print("every other word:", words[0:5:2])
# Often only the step is specified, leaving the other spaces blank, to get regular elements across the whole sequence
print("dny_from_dignity", words[-1][::3])


# TASK 4: Get the word "hue" using every other letter of "households"
answer = words[___][___:___:___]
print(answer)
assert answer == "hue", "Complete task 4 correctly to get past this point"
print("SMASHER, FOURTH POINT SCORED!")

# You can make the step negative to get the sequence in reverse order
# If you do this with start and stop indexes as well, make sure the start is higher than the stop
# Remember, we still stop just before b - but now that means we stop just above b, rather than just below
print("tin from dignity:", words[1][5:2:-1])
# By far the most common way to use this is simply [::-1] to get the whole sequence reversed
print("in backwards:", words[4][::-1])


# TASK 5: Get the acronym "doe" from the word "households"
answer = words[___][___:___:___]
print(answer)
assert answer == "doe", "Complete task 5 correctly to get past this point"
print("VICTORY, FIFTH & FINAL POINT ACHIEVED!")
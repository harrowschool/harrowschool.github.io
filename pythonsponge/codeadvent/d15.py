###########################
# GLOBAL VARIABLES
###########################

result = ""

###########################
# SUBPROGRAMS
###########################


def order_index(char):
    '''Return the index of a character in its custom order.'''
    ORDER = "TINSEL"
    if char in ORDER:
        # it's position in the custom order is its index in the string
        return ORDER.index(char)
    # Characters not in the custom order are sorted alphabetically after those in the custom order
    return len(ORDER) + ord(char)


def compare_words(word1, word2):
    '''Compare two words using the custom order and return -1, 0 or 1 to indicate whether word1 comes before, at the same position or after word2.'''
    
    min_length = min(len(word1), len(word2))
    
    for i in range(min_length):
        if word1[i] != word2[i]:
            if order_index(word1[i]) < order_index(word2[i]):
                return -1
            return 1

    # If all characters up to min_length are the same, then the shorter word comes first
    if len(word1) < len(word2):
        # ==> RETURN THE RIGHT VALUE TO INDICATE THAT word1 COMES BEFORE word2

    elif len(word1) > len(word2):
        # ==> RETURN THE RIGHT VALUE TO INDICATE THAT word1 COMES AFTER word2
    
    # If the words are the same length and all characters are the same, then the words are the same
    return 0


def bubble_sort(words):
    '''Sort a list of words using bubble sort.'''
    for i in range(len(words)):
        for j in range(0, len(words)-i-1):
            if compare_words(words[j], words[j+1]) > 0:
            # ==> SWAP OVER THE TWO WORDS AT POSITIONS j AND j+1 IN THE LIST words


###########################
# MAIN PROGRAM
###########################


# data setup - use example data for testing
data = '''\
SANTA
ELVES
TREE
GIFTS
SLEIGH'''.splitlines()

# uncomment these three lines to use the real challenge data instead when ready
# file = open("d15.txt", "r")
# data = [line.strip() for line in file.readlines()]
# file.close()

bubble_sort(data)

for word in data:
    # ==> COMPLETE THIS NEXT LINE, YOU CAN USE A NEGATIVE INDEX TO GET THE LAST CHARACTER OF A STRING
    result += ________

# output the total
print(result)

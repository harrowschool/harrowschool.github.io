from collections import defaultdict

bag = {}
# Put two apples in the bag
bag["apple"] = 2
# Add two more apples
bag["apple"] += 2

# This next line fails because the value of bag["pear"] isn't defined yet
try:
    bag["pear"] += 2
# The exception thrown when accessing a nonexistent key is a KeyError
except KeyError:
    print("bag['pear'] was not defined")
# That's better
bag["pear"] = 2 + bag.get("pear", 0)

bag.setdefault("orange", 0)
# bag["orange"] was previously undefined so is now 2
print(bag["orange"])
bag.setdefault("apple", 0)
# bag["apple"] was already defined so is unaffected
print(bag["apple"])

# Define a defaultdict with a generator function and a starting dictionary
# Note that int() returns 0, so this dictionary starts with the mappings of the original bag, and automatically defaults
# missing keys to 0
bag = defaultdict(int, bag)
# This now works
bag["banana"] += 2

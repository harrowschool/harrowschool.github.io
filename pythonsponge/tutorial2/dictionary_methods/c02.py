from collections import defaultdict

square = {0: 0, 1: 1, -1: 1, 2: 4, -2: 4}

# Method 1: using a dictionary of sets
inverse_square_1 = {}
for x in square:
    x_squared = square[x]
    # Get the value of inverse_square_1[x_squared], or set it to the empty set if absent
    # Recall that setdefault returns the value for the queried key, whether or not it changed the dictionary. In this
    # case it will return a set. Then use a method of the returned set to immediately add x to it.
    inverse_square_1.setdefault(___, ___).___(x)

print(inverse_square_1)

# Method 2: using a default dictionary of sets. The default value is the empty set.
inverse_square_2 = ___
for x in square:
    x_squared = square[x]
    # Again we get the value at x_squared or automatically set it to the default, then add an x to the returned set
    inverse_square_2[___].___(x)

print(dict(inverse_square_2))

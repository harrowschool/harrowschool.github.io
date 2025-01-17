from functools import reduce


def to_uppercase(string):
    return string.upper()


def concatenate(a, b):
    return a + b


def mirror(string):
    reverse = string[::-1]
    return string + reverse


strings = ["alpha", "bravo", "charlie", "delta"]

for upper in map(to_uppercase, strings):
    print(upper)

print(reduce(concatenate, strings, ""))

for mirrored in map(mirror, strings):
    print(mirrored)

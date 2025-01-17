def make_uppercase(string):
    return string.upper()


animal_names = ["monkey", "dog", "fish", "bird", "leopard", "zebra"]

# No conversion required
for name in map(make_uppercase, animal_names):
    print(name)

# Prints "map object"
print(map(make_uppercase, animal_names))

# Prints a list
print(list(map(make_uppercase, animal_names)))


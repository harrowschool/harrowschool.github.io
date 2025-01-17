# Two lists
names = ["Marco", "Camille", "Manuel", "Ari"]
numbers = ["7700 900077", "7700 900338", "7700 900439", "7700 900932"]
print("Manuel's number is:")
print(numbers[names.index("Manuel")])

# Records
pairs = [('Marco', '7700 900077'), ('Camille', '7700 900338'), ('Manuel', '7700 900439'), ('Ari', '7700 900932')]
print("Camille's number is:")
for name, number in pairs:
    if name == "Camille":
        print(number)
        break

# Dictionary declaration
dictionary = {'Marco': '7700 900077', 'Camille': '7700 900338', 'Manuel': '7700 900439', 'Ari': '7700 900932'}
print("Ari's number is:")
# Dictionary lookup
print(dictionary["Ari"])

# Assignment - same syntax for adding new element or updated existing element
dictionary["Marco"] = "7700 900105"
# Deletion
dictionary.pop("Camille")

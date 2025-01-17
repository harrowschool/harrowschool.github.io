ingredients = [
    "almond paste",
    "sage",
    "plum tomatoes",
    "ancho chile peppers",
    "coriander",
    "honeydew melons",
    "unsweetened chocolate",
]

LONGEST_WORD_LENGTH = 21

# PRINT TABLE HEADER
print("_" * (LONGEST_WORD_LENGTH + 2))
print("|Ingredients" + " " * (LONGEST_WORD_LENGTH - 11) + "|")
print("-" * (LONGEST_WORD_LENGTH + 2))

# PRINT INGREDIENTS
for ingredient in ingredients:
  # THIS NEXT LINE (CURRENTLY COMMENTED OUT) MIGHT BE HELPFUL
  # word_length = len(ingredient)
  next_line = "|" + ingredient + "|"
  print(next_line)

print("-" * (LONGEST_WORD_LENGTH + 2))

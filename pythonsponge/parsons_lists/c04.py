meals = ["fish and chips", "cheeseburger", "cheese on chips", "pizza", "kebab", "cheese on toast", "lettuce"]
filtered_meals = list(meals)
for meal in meals:
  if "cheese" in meal:
    filtered_meals.remove(meal)
print(filtered_meals)
animals = {"Germany": "Black Eagle"}
plants = {"Germany": "Oak"}
# Write a dictionary specifying the capital of Germany (Berlin)
capitals = {___}
categories = {"capital": capitals, "national animal": animals, "national plant": plants}


def update(category):
    country = input("Enter country name: ")
    datum = input(f"Enter the {category} of {country}: ")
    # Update the entry corresponding to `country` in the relevant category dictionary
    categories[category]___ = datum
    print(f"The {category} of {country} is now {datum}")


def remove(category):
    country = input("Enter country name: ")
    # Pop the value corresponding to `country`
    categories[category].___(___)
    print(f"Forgotten the {category} of {country}")


def fetch(category):
    country = input("Enter country name: ")
    # Extract the relevant piece of information
    datum = ___
    print(f"The {category} of {country} is {datum}")


def main():
    tasks = {"1": update, "2": remove, "3": fetch}

    while True:
        for task in tasks:
            print(f"Enter {task} to {tasks[task].__qualname__}")
        print("or 4 to exit")
        task = input("Enter a number: ")
        if task == "4":
            break
        if task not in tasks:
            print("Invalid number")
            continue

        # Iterate through the keys of the categories dictionary
        # You can use .keys() or just iterate through the dictionary directly, which automatically gives keys
        print("Valid categories")
        for ___:
            print(___)
        category = input("Enter a category: ")
        # Validate by running this code only if the inputted category is *not* one of the keys
        # Again you can use .keys() or check membership of the dictionary directly
        if ___:
            print("Invalid category")
            continue

        print("Known countries for this category:")
        print(", ".join(categories[category].keys()))
        tasks[task](category)


main()

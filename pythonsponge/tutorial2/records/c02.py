from collections import namedtuple
from enum import Enum

class Category(Enum):
    NESWPAPERS = 1
    STATIONARY = 2
    CARDS = 3
    BOOKS = 4
    TOYS = 5
    CONFECTIONARY = 6

Product = namedtuple("Product", "name category stock_quantity price")

shop_db = [
    Product("Daily News", Category.NESWPAPERS, 20, 0.65),
    Product("Pencil", Category.STATIONARY, 200, 0.25),
    Product("Birthday Card", Category.CARDS, 150, 1.50),
    Product("Dictionary", Category.BOOKS, 10, 5.00),
    Product("Rubber Duck", Category.TOYS, 50, 2.50),
    Product("Wizzy Chocco Bar", Category.CONFECTIONARY, 500, 0.75),
    Product("Herald Journal", Category.NESWPAPERS, 15, 0.7),
    Product("Pen", Category.STATIONARY, 100, 0.50),
    Product("Christmas Card", Category.CARDS, 100, 1.20),
    Product("Thesaurus", Category.BOOKS, 5, 6.00),
    Product("Teddy Bear", Category.TOYS, 25, 3.50),
    Product("Fizz Chocco Bar", Category.CONFECTIONARY, 300, 0.95)
]

print("Choose a category:")
for category in Category:
    print(f"{category.value}. {category.name}")
category_choice = int(input("Enter a category number that you would like to view: "))

for product in shop_db:
    if product.___________.value == ______________:
        print(f"Name: {___________}, Stock Quantity: {___________}, Price: £{___________:.2f}")



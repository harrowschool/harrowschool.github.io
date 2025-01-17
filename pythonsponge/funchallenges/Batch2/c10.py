import math

UNIT = "#"

def get_distance(point_1, point_2): 
    # HINT: This function can be used to help with the circle printing extension.
    x1, y1 = point_1
    x2, y2 = point_2
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def print_square(side_length):
    # ===> Task 1: Fix the square printing so it is even.
    for _ in range(side_length + 1):
        print(UNIT * side_length)

def print_rectangle(width, height):
    for _ in range(height):
        print(UNIT * width)

def print_circle(radius):
    # ===> EXTENSION: make the circle printing work.
    for y in range(2 * radius + 1):
        for x in range(2 * radius + 1):
            print(UNIT, end="")
        print()

def print_triangle(height):
    for y in range(height):
        for x in range(y + 1):
            print(UNIT, end="")
        print()

has_quit = False

# ===> Task 3: Make it so the user can quit the program by entering "5".
while True:
    choice = input("""Enter a number to choose:
    1) Square
    2) Rectangle
    3) Circle
    4) Triangle
    5) Quit
    """)
    if choice == "1":
        side_length = int(input("Enter side length: "))
        print_square(side_length)
    elif choice == "2":
        width = int(input("Enter width: "))
        height = int(input("Enter height: "))
        # ===> Task 2: Fix the orientation of the rectangle
        print_rectangle(height, width)
    elif choice == "3":
        radius = int(input("Enter radius: "))
        print_circle(radius)
    elif choice == "4":
        height = int(input("Enter height: "))
        print_triangle(height)
    elif choice == "5":
        has_quit = True
    # ===> Task 4: Tell the player if they entered an invalid choice.
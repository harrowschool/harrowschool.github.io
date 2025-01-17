# ==> ADD CODE HERE AT THE START TO CREATE THE Point2D DATACLASS (RECORD)

pt1 = Point2D(x = 3.2, y = -1.6)
pt2 = Point2D(x = -2.1, y = 4.3)

dist = ((pt1.x - pt2.x) ** 2 + (pt1.y - pt2.y) ** 2) ** 0.5

print(f"The distance between the two points is {dist:.2f}")

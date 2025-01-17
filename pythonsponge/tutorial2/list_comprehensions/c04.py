grid = [
    [
        "+" if (row + col) % _ == 0 else "-"
        for ___ in range(10)
    ]
    for _________________
]

print("\n".join(["".join(___) for row in grid]))
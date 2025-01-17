'''Expression Tree'''

# Fill in None to indicate there is no child node on that branch
expr_tree = [
    ("*", __, 2),         # row 0
    ("-", 3, 4),          # row 1
    ("-", 5, _),          # row 2
    ("+", 7, 8),          # row 3
    ("/", 9, 10),         # row 4
    ("5", __, None),      # row 5
    ("4", None, None),    # row 6
    ("7", None, None),      # row 7
    ("*", 11, 12),        # row 8
    ("+", __, __),        # row 9
    ("+", __, 16),        # row 10
    ("18", None, None),   # row 11
    ("3", None, None),    # row 12
    ("5", None, None),    # row 13
    ("__", None, None),   # row 14
    ("1", None, __),      # row 15
    ("2", None, None)     # row 16
]

'''Tree Traversal'''

root = 0


def post_order_traverse(curr):

  left, right = expr_tree[____][1], expr_tree[____][2]

  if left != ____:
    post_order_traverse(left)

  if right != None:
    post_order_traverse(____)

  print(expr_tree[curr][____])


post_order_traverse(____)

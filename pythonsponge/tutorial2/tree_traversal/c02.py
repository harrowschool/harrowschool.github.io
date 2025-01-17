'''Tree Representation'''

tree = [
    ("A", ____, 7),     # index 0
    ("B", 3, 2),        # index 1
    ("C", 11, ____),    # index 2
    ("D", None, None),  # index 3
    ("E", ____, None),  # index 4
    ("F", 9, ____),     # index 5
    ("G", None, None),  # index 6
    ("H", 6, 8),        # index 7
    ("I", ____, 5),     # index 8
    ("J", None, None),  # index 9
    ("K", None, None),  # index 10
    ("L", None, ____)   # index 11
]

'''Tree Traversal Algorithms'''

root = 0


def pre_order(curr):

  print(tree[curr][____], end=" ")

  left, right = tree[____][1], tree[curr][____]

  if left is not None:
    ________(left)

  if right is not None:
    pre_order(right)


def in_order(curr):

  left, right = tree[curr][1], tree[curr][____]

  if left is not ____:
    in_order(left)

  print(tree[____][0], end=" ")

  if right is not ____:
    _______(right)


def post_order(curr):

  left, right = tree[curr][____], tree[curr][2]

  if ____ is not None:
    post_order(left)

  if ____ is not None:
    ______(right)

  print(tree[curr][0], end=" ")


pre_order(root)
print()
in_order(root)
print()
post_order(____)
print()

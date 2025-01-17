'''Binary Search Tree'''

tree = [
    (216, ____, 2),     # index 0
    (143, 3, None),     # index 1
    (316, 4, ____),     # index 2
    (90, None, 6),      # index 3
    (248, ____, 7),     # index 4
    (952, 8, 9),        # index 5
    (96, None, None),   # index 6
    (306, None, ____),  # index 7
    (687, ____, 11),    # index 8
    (961, None, None),  # index 9
    (327, None, ____),  # index 10
    (758, None, None),  # index 11
]

'''In-Order Traversal'''

root = ____


def in_order(curr):

  left, right = tree[____][1], tree[curr][____]

  if left is not ____:
    ______(left)

  print(tree[curr][____], end=" ")

  if ____ is not None:
    in_order(____)


in_order(root)

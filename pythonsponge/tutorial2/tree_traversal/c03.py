'''Binary Search Tree'''

# None is used to indicate there is no child node for the given node
tree = [
    (10, 1, 2),         # index 0
    (5, 3, 4),          # index 1
    (17, 5, 6),         # index 2
    (3, 7, 8),          # index 3
    (8, 9, 10),         # index 4
    (13, 11, 12),       # index 5
    (19, 13, 14),       # index 6
    (1, None, None),    # index 7
    (4, None, None),    # index 8
    (6, None, None),    # index 9
    (9, None, None),    # index 10
    (11, None, None),   # index 11
    (15, None, None),   # index 12
    (18, None, None),   # index 13
    (21, None, None)    # index 14
]

'''In-Order Traversal'''

root = 0


def in_order(curr):

  left, right = tree[curr][1], tree[curr][2]

  if left is not None:
    in_order(left)  # 1. Traverse left subtree

  print(tree[curr][0], end=" ")  # 2. Traverse root node

  if right is not None:
    in_order(right)  # 3. Traverse right subtree


in_order(root)

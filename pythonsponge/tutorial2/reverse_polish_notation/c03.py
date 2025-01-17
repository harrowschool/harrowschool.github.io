'''Expression Tree'''

# First index = symbol, Second index = index of left node, Third index = index of right node
# None is used to indicate there is no child node on that branch
expr_tree = [
    ("*", 1, 2),        # row 0
    ("+", 3, 4),        # row 1
    ("+", 5, 6),        # row 2
    ("3", None, None),  # row 3
    ("4", None, None),  # row 4
    ("1", None, None),  # row 5
    ("2", None, None)   # row 6
]

'''Tree Traversal'''

root = 0

# Recursive Tree Traversal


def post_order_traverse(curr):

  left, right = expr_tree[curr][1], expr_tree[curr][2]

  if left != None:
    post_order_traverse(left)  # traverse from left child node

  if right != None:
    post_order_traverse(right)  # traverse from right child node

  print(expr_tree[curr][0], end=" ")  # output current node


post_order_traverse(root)

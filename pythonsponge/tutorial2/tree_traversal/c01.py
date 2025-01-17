'''Tree Representation'''

# None is used to indicate there is no child node for the given node
tree = [
    (0, 1, 2),          # index 0
    (1, 3, 4),          # index 1
    (2, 5, 6),          # index 2
    (3, None, None),    # index 3
    (4, None, None),    # index 4
    (5, None, None),    # index 5
    (6, None, None),    # index 6
    (7, None, None)     # index 7
]

'''Tree Traversal Algorithms'''

root = 0

# Pre Order Traversal
def pre_order(curr):

    print(tree[curr][0], end=" ") # 1. Traverse root node

    left, right = tree[curr][1], tree[curr][2]

    if left is not None:
        pre_order(left) # 2. Traverse left subtree
    
    if right is not None:
        pre_order(right) # 3. Traverse right subtree

# In Order Traversal
def in_order(curr):

    left, right = tree[curr][1], tree[curr][2]

    if left is not None:
        in_order(left) # 1. Traverse left subtree

    print(tree[curr][0], end=" ") # 2. Traverse root node

    if right is not None:
        in_order(right) # 3. Traverse right subtree

# Post Order Traversal
def post_order(curr):

    left, right = tree[curr][1], tree[curr][2]

    if left is not None:
        post_order(left) # 1. Traverse left subtree

    if right is not None:
        post_order(right) # 2. Traverse right subtree
    
    print(tree[curr][0], end=" ") # 3. Traverse root node


print("Pre Order: ", end="")
pre_order(root)
print()

print("In Order: ", end="")
in_order(root)
print()

print("Post Order: ", end="")
post_order(root)
print()
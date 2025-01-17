# place left child of node at index i at index 2i+1
# place right child of node at index i at index 2i+2
# greatest index needed is 2^10

digits = map(int, list(input()))
row = int(input())

tree = [None] * 1024

for digit in digits:
    curr = 0
    while tree[curr] != None:
        curr = 2 * curr + (1 if digit < tree[curr] else 2)
    tree[curr] = digit

print(*filter(lambda x: x != "None", map(str, tree[2 ** (row-1) - 1: 2 ** row - 1])))

# ALSO CONSIDER

'''
from collections import defaultdict

depths = defaultdict(list)

def insert(node, n, depth):
  val = node.get("n",None)
  if val == None:
    node |= {"n":n, 0:{}, 1:{}}
    depths[depth].append(n)
  else:
    insert(node[n > val], n, depth+1)
      
digits = [int(i) for i in input()]
tree = {}
for d in digits:
  insert(tree,d,1)

print(*sorted(depths[int(input())]))
'''
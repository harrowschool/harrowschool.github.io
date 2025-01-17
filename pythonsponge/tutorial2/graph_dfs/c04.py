'''Graph'''

# adjacency list with neighbours in ascending order
graph = {
    1: [3, 6],
    2: [8, 10],
    3: [1, 7, 10, 11],
    4: [10],
    5: [9, 11],
    6: [1],
    7: [3, 8],
    8: [2, 7, 9, 11],
    9: [5, 8, 10],
    10: [2, 3, 4, 9],
    11: [3, 5, 8, 12],
    12: [11]
}

'''Main Algorithm'''


def dfs(graph, curr, visited=set()):

  # print current node and add to visited
  print(____)
  visited.add(____)

  for neighbour in _____[_____]:
    if ______ not in visited:
      dfs(graph, _____, _____)


# traverse from node 1
dfs(graph, 1)

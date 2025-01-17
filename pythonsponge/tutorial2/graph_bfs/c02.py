from collections import deque

'''Graph'''

graph = {
    1: [2, 3, 9],
    2: [1, 6],
    3: [__, 4, 8],
    4: [3, 5, __],
    5: [4, 11],
    6: [2, __, 8, 10],
    7: [__, 11],
    8: [3, 6],
    9: [__],
    10: [6, 7],
    11: [5, 7, 12],
    12: [11]
}

'''Main Algorithm'''


def bfs(graph, start):

  queue = _____([start])  # create deque with start node
  visited = set()

  while queue:

    curr = queue.popleft()

    if curr not in _____:

      print(curr)  # print when node is visited
      ______.add(curr)

      for neighbour in _____[curr]:
        if _____ not in visited:
          _______.append(neighbour)


# traverse from node 1
bfs(graph, 1)

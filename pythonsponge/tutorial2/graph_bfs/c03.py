from collections import deque

'''Graph'''

# Graph represented as an adjacency list
graph = {
    1: [8, 9],
    2: [3, 4, 5, 6, 7],
    3: [2, 4, 9],
    4: [2, 3, 8],
    5: [2, 7],
    6: [2],
    7: [2, 5],
    8: [1, 4],
    9: [1, 3]
}

'''Main Algorithm'''


def bfs_shortest_path(graph, start, goal):
  queue = deque([[start]])
  visited = set()

  while queue:
    path = queue.popleft()
    node = path[-1]

    if node == goal:
      return path

    elif node not in visited:
      for neighbor in graph[node]:
        queue.append(path + [neighbor])

      visited.add(node)

  return None  # if no path exists


# find shortest path from node 5 to 8
print(bfs_shortest_path(graph, 5, 8))

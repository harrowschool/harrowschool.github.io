from collections import deque

'''Disconnected Graph'''

graph = {
    'A': ['B'],
    'B': ['A'],
    'C': ['D'],
    'D': ['C'],
    'E': [],
    'F': ['G', 'H'],
    'G': ['F'],
    'H': ['F']
}


'''Main Algorithm'''


def bfs_num_connected_components(graph):
  visited = set()
  result = 0

  while len(visited) < len(graph):

    # pick an unvisited node
    start = (graph.keys() - visited).pop()

    queue = deque([_____])

    # perform bfs to visit all nodes in the connected component
    while queue:
      node = queue._______()
      if node not in _______:
        visited.add(node)
        for neighbour in set(graph[node]) - visited:
          queue.append(_________)

    # increment the number of connected components
    result += _

  return result


# find the number of connected components in the graph
print(bfs_num_connected_components(graph))

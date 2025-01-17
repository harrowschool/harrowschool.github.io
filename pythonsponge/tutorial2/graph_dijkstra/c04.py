from heapq import heappop, heappush

'''Graph'''

graph = {0: [(__, 5), (5, 15), (8, 14)],
         1: [(0, 5), (2, 13), (5, 10), (9, 8)],
         2: [(1, 13), (3, 12), (5, 4), (6, __), (2, 4)],
         3: [(2, 12), (4, 10), (6, 3), (9, 16)],
         4: [(__, 10), (6, 20), (7, 14)],
         5: [(0, 15), (1, 10), (2, 4), (6, 12), (7, 17), (8, 3)],
         6: [(2, 7), (3, 3), (4, 20), (5, 12), (7, 9), (8, 12)],
         7: [(4, 14), (5, 17), (6, 9), (8, 19)],
         8: [(0, 14), (5, 3), (6, 12), (7, __)],
         9: [(__, 8), (2, 4), (3, 16)]
         }

'''Initialisation'''

num_nodes = len(graph)

# just use a normal list of (distance, node) tuples along with heappop and heappush to achieve a priority queue
priority_queue = [(0, 0)]  # starting with distance 0 from node 0
target = 4

visited = [_____] * num_nodes

distances = [float("inf")] * num_nodes
distances[____] = _____

previous = [-1] * num_nodes

'''Main Algorithm'''

while ____________:

  dist, curr = heappop(priority_queue)

  if curr == target:
    break

  elif not visited[curr]:
    ______[curr] = True

    for neighbour, weight in graph[______]:
      if not visited[_____] and weight + dist < _____[______]:
        heappush(priority_queue, (______ + ____, neighbour))
        distances[neighbour] = ______ + ____
        previous[neighbour] = ______

'''Shortest Path Calculation'''

path, curr = [target], target
while previous[curr] != -1:
  curr = _______[curr]
  path.append(curr)

path.reverse()
print(_______)

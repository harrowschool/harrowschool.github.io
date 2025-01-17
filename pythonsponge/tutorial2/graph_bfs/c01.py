# deque is a 'double ended queue' which is better than using a list for queue purposes
# because it supports efficient append and pop operations from both ends
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


def bfs(graph, start):

  queue = deque([start])  # initialise the queue with the start node in it
  visited = set()  # visited nodes
  traversal = []  # traversal order

  # TRACING ONLY
  trace_mode = input(
      "Do you want to trace the algorithm? (y/n): ").lower() == "y"
  if trace_mode:
    print("Press enter to go to the next step")
    print(f"\n{'Node':<5} | {'Queue'}")
    print("-"*30)

  while queue:

    curr = queue.popleft()  # dequeue

    if curr not in visited:  # if not visited

      traversal.append(curr)  # add to traversal
      visited.add(curr)  # add to visited

      for neighbour in graph[curr]:  # loop through all neighbours
        if neighbour not in visited:  # if neighbour is not visited
          queue.append(neighbour)  # enqueue neighbour

      # TRACING ONLY
      if trace_mode:
        input(f"{curr:<5} | {queue}")

  return traversal  # return the traversal order


print(bfs(graph, 1))  # traverse from node 1

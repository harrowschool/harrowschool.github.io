from queue import PriorityQueue  # priority queue operations

'''Graph'''

# Graph represented as adjacency list:
# - key = node number
# - value = (neighbour number, weight)
graph = {0: [(1, 4), (7, 8)],
         1: [(0, 4), (2, 8), (7, 11)],
         2: [(1, 8), (3, 7), (5, 4), (8, 2)],
         3: [(2, 7), (4, 9), (5, 14)],
         4: [(3, 9), (5, 10)],
         5: [(2, 4), (3, 14), (4, 10), (6, 2)],
         6: [(5, 2), (7, 1), (8, 6)],
         7: [(0, 8), (6, 1), (8, 7)],
         8: [(2, 2), (6, 6), (7, 7)]
         }

'''Initialisation'''

priority_queue = PriorityQueue()  # priority queue of (distance, node) tuples
priority_queue.put((0, 0))  # starting with distance 0 from node 0

visited = [False] * len(graph)  # visited nodes array
distances = [float("inf")] * len(graph)  # distances array
distances[0] = 0  # we start from node 0

target = 4  # target node

# TRACING ONLY
trace_mode = input(
    "Do you want to trace the algorithm? (y/n): ").lower() == "y"
step = 0

if trace_mode:
  print("Press enter to go to next step")
  print(f"{'STEP':<5}| {'(NODE, DIST) ':<14}| {'VISITED':<26}| {'DISTANCES':<45}")
  print("-" * 110)
  visited_print = ", ".join(['T' if entry else 'F' for entry in visited])
  print(f"{step:<5}| {'(None, None)':<14}| {visited_print:<26}| {str(distances):<45}")

'''Main Algorithm'''

while not priority_queue.empty():  # while there are items in the priority queue

  dist, curr = priority_queue.get()  # get node with lowest distance from node 0

  if curr == target:  # if target node reached
    break

  elif not visited[curr]:  # if not visited
    visited[curr] = True  # set visited to true

    for neighbour, weight in graph[curr]:  # loop through all neighbours
      # if neighbour not visited and shorter path found
      if not visited[neighbour] and weight + dist < distances[neighbour]:
        priority_queue.put((weight + dist, neighbour))  # put to queue
        distances[neighbour] = weight + dist  # update distance

    # TRACING ONLY
    step += 1
    if trace_mode:
      visited_print = ", ".join(
          ['T' if entry else 'F' for entry in visited])
      input(
          f"{step:<5}| {f'({curr}, {dist})':<14}| {visited_print:<26}| {str(distances):<45}")

print("Minimum distance to target node", target, "is", distances[target])

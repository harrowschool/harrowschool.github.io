from queue import PriorityQueue

'''Graph'''

graph = {0: [(__, 5), (5, 15), (8, 14)],
         1: [(0, 5), (2, 13), (5, 10), (9, 8)],
         2: [(1, 13), (3, __), (5, 4), (6, __), (2, 4)],
         3: [(2, 12), (4, 10), (6, 3), (9, 16)],
         4: [(__, 10), (6, 20), (7, 14)],
         5: [(0, 15), (1, 10), (__, 4), (6, 12), (7, 17), (8, 3)],
         6: [(2, 7), (3, 3), (4, 20), (5, 12), (7, 9), (8, 12)],
         7: [(4, 14), (5, __), (6, 9), (8, 19)],
         8: [(0, 14), (5, 3), (6, 12), (7, __)],
         9: [(__, 8), (2, 4), (3, 16)]
         }

'''Initialisation'''

num_nodes = len(graph)
priority_queue = _________()
priority_queue.put((0, 0))
visited = [_____] * num_nodes
distances = [float("inf")] * ______
distances[____] = ____

'''Main Algorithm'''

while not priority_queue.empty():

    dist, curr = _________.get()

    if not visited[curr]: 
        ______[curr] = True 

        for neighbour, weight in _____[curr]:
            if not visited[______] and _____ + _____ < distances[neighbour]: 
                priority_queue.put((weight + dist, neighbour))
                _____[neighbour] =_____ + _____

print(distances[4])
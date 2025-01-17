'''Graph'''

# adjacency list with neighbours in ascending order
# ==> fill in the blanks to represent the given graph diagram
graph = {
    1: [3, 6],
    2: [8, 10],
    3: [1, 7, 10, __],
    4: [10],
    5: [9, 11],
    6: [1],
    7: [__, 8],
    8: [2, 7, __, 11],
    9: [5, __, 10],
    10: [__, 3, 4, 9],
    11: [3, 5, 8, 12],
    12: [11]
}

'''Main Algorithm'''

# ==> rearrange the lines and correct the indentation

stack.append(neighbour)
print(current_node)  # Process the current node
for neighbour in graph[current_node]:
stack = [1]  # Start from vertex 1
visited[current_node] = True
if not visited[neighbour]:
current_node = stack.pop()
visited = [False] * (len(graph) + 1)
if not visited[current_node]:
while len(stack) > 0:

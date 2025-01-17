'''Graph'''

# Graph represented as an adjacency list
graph = {
    1: [3, 4, 5, 6, 8],
    2: [4, 5],
    3: [1, 7],
    4: [1, 2],
    5: [1, 2, 8],
    6: [1, 8],
    7: [3],
    8: [1, 5, 6]
}

'''Main Algorithm'''

# Initialize a stack with a chosen starting node
stack = [1]  # Start from node 1
visited = set()

# Perform DFS
while stack:

  current_node = stack.pop()

  if current_node not in visited:

    print(current_node)  # Process the current node
    visited.add(current_node)

    # Add unvisited adjacent nodes to the stack
    stack.extend(set(graph[current_node]) - visited)
    # or you can can replace the above line with:
    stack.extend(graph[current_node])
    # and rely instead on the previous check to filter out duplicates
    # but with potentially more memory used by the stack

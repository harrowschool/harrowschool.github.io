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

'''Tracing Setup'''
trace_mode = input(
    "Do you want to trace the algorithm? (y/n): ").lower() == "y"

if trace_mode:
  print("Press enter to go to the next step")
  print(f"\n{'Call Number':<10} | {'Current Node':<10}")
  print("-"*27)

call_numbers = {}

'''Main Algorithm'''


def dfs(graph, curr, visited=set()):  # Recursive DFS

  path = [str(curr)]  # initialise path
  visited.add(curr)  # mark current node as visited

  # TRACING ONLY
  if trace_mode:
    if curr not in call_numbers:
      call_numbers[curr] = len(visited)
    input(f"{call_numbers[curr]:<11} | {curr}")

  for neighbour in graph[curr]:  # look at all neighbours
    if neighbour not in visited:  # if not visited
      # traverse neighbour and add to path
      path.extend(dfs(graph, neighbour, visited))

      # TRACING ONLY
      if trace_mode:
        input(f"{call_numbers[curr]:<11} | {curr} (backtrack)")

      path.append(str(curr))  # append backtrack to path

  return path


# traverse from node 1
print("Path including backtracking:", ",".join(dfs(graph, 1)))

graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}

def dfs_recursive(graph, node, visited = []):
  if node not in visited:
    visited.append(node)
    print(node)
    for neighbor in graph[node]:
      dfs_recursive(graph, neighbor, visited)


def dfs_iterative(node):
  visited = []
  stack = []

  stack.append(node)

  while stack:
    val = stack.pop(0)
    print(val)
    visited.append(val)
    
    for neighbor in graph[val]:
      if neighbor not in visited:
        stack.insert(0, neighbor)

dfs_recursive(graph, 'A')
print('-----')
dfs_iterative('A')
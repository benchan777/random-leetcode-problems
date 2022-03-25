def numberOfConnections(gridOfNodes):
  total_connections = 0
  node_dict = {}

  for i in range(len(gridOfNodes)):
    node_dict[i] = 0
    for node in gridOfNodes[i]:
      if node == 1:
        node_dict[i] += 1

  i = 0
  last_node_count = 0

  while i < len(gridOfNodes) - 1:
    if node_dict[i] != 0:
      last_node_count = node_dict[i]

    total_connections += (last_node_count * node_dict[i + 1])
    i += 1

  return total_connections

print(numberOfConnections([[1,1,1],[0,1,0],[0,0,0],[1,1,0]]))
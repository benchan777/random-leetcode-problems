graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}

queue = []
visited = []

def bfs(graph, vertex, index = 0):
    if not visited and not queue:
        queue.append(vertex)
        visited.append(vertex)

    if not queue: # If queue is empty, we have finished traversing all nodes
        return visited

    else:
        if index < len(graph[vertex]): # Iterate through all neighbors of current vertex
            if graph[vertex][index] not in visited: # Only enqueue values that have not been visited
                queue.append(graph[vertex][index])
                visited.append(graph[vertex][index])
            return bfs(graph, vertex, index + 1)

        else:
            dequeue = queue.pop(0)
            if not queue: # If queue is empty, we have finished traversing all nodes
                return visited
            else:
                return bfs(graph, queue[0], index = 0)

print(bfs(graph, 'A'))
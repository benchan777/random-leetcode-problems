graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}

stack = []
visited = []

def dfs(graph, vertex, index = 0):
    if not visited and not stack:
        stack.insert(0, vertex)
        visited.append(vertex)

    if not stack:
        return visited

    else:
        if len(graph[vertex]) > 0:
            if index == len(graph[vertex]):
                stack.pop(0)
                if not stack:
                    return visited
                return dfs(graph, stack[0], index = 0)

            if graph[vertex][index] not in visited:
                stack.insert(0, graph[vertex][index])
                visited.append(graph[vertex][index])
                return dfs(graph, stack[0], index = 0)
            else:
                return dfs(graph, stack[0], index + 1)

        else:
            stack.pop(0)
            return dfs(graph, stack[0], index = 0)

print(dfs(graph, 'A'))
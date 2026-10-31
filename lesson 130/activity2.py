graph = {
    'A' : ['B', 'C'],
    'B' : ['A', 'D', 'E'],
    'C' : ['A', 'F'],
    'D' : ['B'],
    'E' : ['B', 'F'],
    'F' : ['C', 'E']
}

visited = set()

stack = ['A']
while stack:
    node = stack.pop()
    if node not in visited:
        print(node, end=" ")
        visited.add(node)

        for neighbour in reversed(graph[node]):
            if neighbour not in visited:
                stack.append(neighbour)
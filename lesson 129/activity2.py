from collections import deque
graph = {
    'A' : ['B', 'C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : [],
    'F' : []
}

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)

            for neighbour in graph[node]:
                if neighbour not in visited:
                    queue.append(neighbour)
    max_node_s = [0]
    max_degree = -1
    for node in graph:
        degree = len(graph[node])
        if degree > max_degree:
            max_degree = degree
            node = max_node_s.popleft()
            max_node_s.add(node)
        elif degree == max_degree:
            max_node_s.add(node)

         
bfs(graph, 'B') 
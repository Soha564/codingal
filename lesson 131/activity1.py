from collections import deque
graph = {
    'A' : ['B', 'C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : [],
    'F' : []
}
visited = set()
queue = [('A', 0)]
visited.add('A')
level_2_nodes = []
count = 0
while queue:
    node, level = queue.pop(0)
    print(node, end=" ")
    if level == 2:
        count += 1
        level_2_nodes.append(node)
    for neighbour in graph[node]:
        if neighbour not in visited:
            visited.add(neighbour)
            queue.append((neighbour, level +1))
print("\nNumber of nodes at level 2: ", count)
print("Nodes at level 2: ", level_2_nodes)
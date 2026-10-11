class Graph:
    def __init__(self):
        self.graph = {}
    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        
        self.graph[u].append(v)

    def display(self):
        for node in self.graph:
            print(node, "->", self.graph[node])

g = Graph()
g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(1,2)
g.add_edge(2,3)
g.add_edge(3,4)

g.display()
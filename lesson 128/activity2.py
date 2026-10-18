class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Graph:
    def __init__(self, n):
        self.n = n
        self.graph = [None] * n

    def add_edge(self, u, v):
        new_node = Node(v)
        new_node.next = self.graph[u]
        self.graph[u] = new_node

    def print_graph(self):
        for i in range(self.n):
            print(i, "->", end=" ")

            temp = self.graph[i]
            count = 0
            while temp:
                print(temp.data, end=" -> ")
                count += 1
                temp = temp.next
            print("None")
            print(i, "-", count)
    def checker(self, num1, num2):
        temp = self.graph[num1]
        while temp:
            if temp.data == num2:
                print("True")
                return 
            temp = temp.next
        print("False")

g = Graph(4)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.print_graph()
g.checker(0, 1)
g.checker(2, 4)
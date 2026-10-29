class FibonacciNode:
    def __init__(self, key):
        self.key = key
        self.degree = 0
        self.parent = None
        self.child = None
        self.left = self
        self.right = self


class FibonacciHeap:
    def __init__(self):
        self.min_node = None
        self.total_nodes = 0

    def insert(self, key):
        node = FibonacciNode(key)

        if self.min_node is None:
            self.min_node = node
        else:
            node.left = self.min_node
            node.right = self.min_node.right
            self.min_node.right.left = node
            self.min_node.right = node

            if node.key < self.min_node.key:
                self.min_node = node

        self.total_nodes += 1

    def display(self):
        if self.min_node is None:
            print("Heap is empty")
            return

        print("Root List:", end=" ")
        current = self.min_node
        while True:
            print(current.key, end=" ")
            current = current.right
            if current == self.min_node:
                break
        print()

fib_heap = FibonacciHeap()

elements = [10, 3, 15, 6, 21, 1]

print("Inserting elements:")
for element in elements:
    print(element, end=" ")
    fib_heap.insert(element)

print("\n")
fib_heap.display()

print("Minimum element:", fib_heap.min_node.key)
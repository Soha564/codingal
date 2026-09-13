class Miniheap: 
    def __init__(self):
        self.heap = []
    def insert(self, val):
        self.heap.append(val)
        i = len(self.heap) - 1
        while i > 0:
            parent = (i-1) // 2

            if self.heap[i] < self.heap[parent]:
                self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]

                i = parent
            else:
                break
    def display(self):
        print(self.heap)
        print("Min walue: ", self.heap[0])

h = Miniheap()

h.insert(30)
h.insert(10)
h.insert(20)
h.insert(5)
h.insert(15)

h.display()

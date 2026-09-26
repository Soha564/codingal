class Maxheap: 
    def __init__(self):
        self.heap = []
    def insert(self, val):
        self.heap.append(val)
        i = len(self.heap) - 1
        while i > 0:
            parent = (i-1) // 2

            if self.heap[i] > self.heap[parent]:
                self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]

                i = parent
            else:
                break
    def display(self):
        print(self.heap)
        print("Max value:", self.heap[0])

    def delete(self, val):
        if val not in self.heap:
            print(val, "not found in heap.")
            return
        index = self.heap.index(val)
        last = self.heap[-1] 
        self.heap[index] = last
        self.heap.pop()

    def heapify(self, i):
        n = len(self.heap)
        while true:
            largest = i
            left = 2*i + 1
            right = 2*1 + 2

            if left < n and heap[left] > heap[largest]:
                largest = left
            if right < n and heap[right] > heap[largest]:
                largest = right
            if largest == 1:
                break

            heap[i], heap[largest] = heap[largest], heap[i]

            i = largest



h = Maxheap()

h.insert(30)
h.insert(10)
h.insert(20)
h.insert(25)
h.insert(5)
h.delete(10)

h.display()
import heapq
def sortArrayInDescendingOrder():
    MinHeap = []
    heapq.heappush(MinHeap, 5)
    print(MinHeap)
    heapq.heappush(MinHeap, 6)
    print(MinHeap)
    heapq.heappush(MinHeap, 8)
    print(MinHeap)
    heapq.heappush(MinHeap, 2)
    print(MinHeap)
    heapq.heappush(MinHeap, 3)
    print(MinHeap)
    smallest = heapq.heappop(MinHeap)
    print(smallest)

sortArrayInDescendingOrder()

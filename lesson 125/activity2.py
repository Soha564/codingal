import heapq
queue = []
def enqueue(item, priority):
    heapq.heappush(queue, (priority, item))
def dequeue(queue):
    if queue:
        print(queue[0], "removed.")
        return heapq.heappop(queue)


enqueue("Task B", 1)
enqueue("Task C", 2)
enqueue("Task A", 2)
print(queue)
dequeue(queue)
print(queue)
dequeue(queue)
print(queue)
    
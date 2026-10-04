queue = []
def enqueue(item, priority):
    queue.insert(priority-1, item)
def dequeue(queue):
    if len(queue) == 0:
        print("Queue is empty.")
    print(queue[0], "removed")
    return queue.pop(0)

enqueue("Task A", 3)
enqueue("Task B", 1)
enqueue("Task C", 2)
print(queue)
dequeue(queue)
print(queue)
dequeue(queue)
print(queue)
    
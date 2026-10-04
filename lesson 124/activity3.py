import heapq
def sortArrayInDescendingOrder(arr):
    MinHeap = []
    for num in arr:
        heapq.heappush(MinHeap, num)
    
    result = []
    print(heapq.nlargest(2,MinHeap)) # prints the 2 largest elements
    while MinHeap:
        top = heapq.heappop(MinHeap)
        result.insert(0, top)
    return result

if __name__ == '__main__':
    arr = [4, 6, 3, 2, 7, 9]
    result = sortArrayInDescendingOrder(arr)

    for num in result:
        print(num, end=' ')
    print()
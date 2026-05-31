def partition(arr, low, high):
    mid = (low+high)// 2
    pivot  = arr[mid]
    arr[mid], arr[low] = arr[low], arr[mid]

    left = low + 1
    right = high
    while True:
        while left <= right and arr[left] <= pivot:
            left = left + 1
        
        while left <= right and arr[right] > pivot:
            right = right - 1

        if left > right:
            break
        else:
            arr[left], arr[right] = arr[right], arr[left]
    arr[low], arr[right] = arr[right], arr[ low]
    
    return right
def quick_sort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)

        quick_sort(arr, low, p - 1)

        quick_sort(arr, p+1, high)

arr = [45, 23, 78, 12, 56, 89, 34, 67]
print("Original Array:")
print(arr)

quick_sort(arr, 0, len(arr) -1)

print("\nSorted Arrar:")
print(arr)
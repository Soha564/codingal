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

arr = []
num = int(input("Enter how long you would like the array to be:"))
print("Enter", num, "numbers.")
for _ in range(num):
    h = input()
    arr.append(h)
print("Original Array:")
print(arr)

quick_sort(arr, 0, num -1)

print("\nSorted Arrar:")
print(arr)
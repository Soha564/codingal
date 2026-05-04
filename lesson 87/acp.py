def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr



n = int(input("Enter size of array: "))
print("Start entering elements of array, each element in a new line:\n")
arr = []
for _ in range(n):
    arr.append(int(input()))
sorted_arr = selection_sort(arr)
print("\nSorted Array:")
for num in sorted_arr:
    print(num, end=" ")

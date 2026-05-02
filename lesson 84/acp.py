def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


arr = [32, 45, 63, 77, 82]
target = int(input("Enter a number:"))

index = binary_search(arr, target)
print("Element found at index:", index)

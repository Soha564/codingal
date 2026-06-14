def left_rotate(arr, n):
    for i in range(n):
        num = arr[0]
        for j in range(1, len(arr)):
            arr[j-1] = arr[j]
        arr[-1] = num
    
    return arr
arr = [4, 2, 0, 6, 1, 8, 3, 10, 5 , 6]
n = int(input("Enter a number:"))
print("Before rotation:", arr)
result = left_rotate(arr, n)
print("After rotation:", result)
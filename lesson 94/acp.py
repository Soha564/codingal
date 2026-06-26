def left_rotate(arr, n):
    for i in range(n):
        num = arr[0]
        for j in range(1, len(arr)):
            arr[j-1] = arr[j]
        arr[-1] = num
    
    return arr
arr = []
num = int(input("Enter a number:"))
n = int(input("Enter another number:"))
print("Keep entering number:")
for _ in range(num):
    a = int(input())
    arr.append(a)
print("Before rotation:", arr)
result = left_rotate(arr, n)
print("After rotation:", result)
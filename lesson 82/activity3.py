def mulitply(arr):
    arr_size = len(arr)
    result = []
    for i in range(arr_size):
        count = 1
        for j in range(arr_size):
            if j != i:
                count *= arr[j]
        result.append(count)
    return result
arr = [1, 2, 3, 4]
print(mulitply(arr))
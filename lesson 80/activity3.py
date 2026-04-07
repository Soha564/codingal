def move_all_zeroes_to_end(arr):
    n = len(arr)
    i = 0
    while i < n:
        if arr[i] == 0:
            arr.pop(i)
            arr.append(0)
            n = n-1
        else:
            i += 1
    return arr
arr = [0, 1, 0, 0, 0, 86, 3, 1, 0, 2]
print(move_all_zeroes_to_end(arr))

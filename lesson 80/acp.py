def move_all_ZeroesOnesandTwos_to_end(arr):
    for j in range(0, 3):
        n = len(arr)
        i = 0
        while i < n:
            if arr[i] == j:
                arr.pop(i)
                arr.append(j)
                n = n-1
            else:
                i += 1
    return arr
arr = [0, 1, 0, 1, 0, 1, 2, 0, 1, 2, 1, 0, 2]
print(move_all_ZeroesOnesandTwos_to_end(arr))
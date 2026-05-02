def closest_pair(arr):
    arr.sort() 
    min_diff = float('inf')
    pair = ()

    for i in range(len(arr) - 1):
        diff = abs(arr[i] - arr[i + 1])
        if diff < min_diff:
            min_diff = diff
            pair = (arr[i], arr[i + 1])

    return pair


arr = [7, 18, 65, 84, 87, 91, 99, 113]
result = closest_pair(arr)
print("Closest pair is:", result)

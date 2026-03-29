def find_missing(arr):
    n = len(arr) + 1
    expected_sum = n * (n + 1) // 2
    return expected_sum - sum(arr)

print(find_missing([1, 4, 3, 2, 6]))
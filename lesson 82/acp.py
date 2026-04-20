def print_flips(arr):
    n = len(arr)
    zero_groups = 0
    one_groups = 0
    for i in range(1, n):
        if arr[i] != arr[i-1]:
            if arr[i-1] == 0:
                zero_groups += 1
            else:
                one_groups += 1
    if arr[-1] == 0:
        zero_groups += 1
    else:
        one_groups += 1
    flip_value = 0 if zero_groups < one_groups else 1
    i = 0
    while i < n:
        if arr[i] == flip_value:
            start = i
            while i < n and arr[i] == flip_value:
                i += 1
            end = i - 1
            print(f"From {start+1} to {end+1}")
        else:
            i += 1
arr = [0, 1, 1, 0, 0, 1, 1]
print_flips(arr)

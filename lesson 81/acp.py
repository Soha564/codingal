def longest_odd_even_subarray(a):
    if not a:
        return 0

    max_len = 1
    curr_len = 1

    for i in range(1, len(a)):
        if (a[i] % 2) != (a[i - 1] % 2):
            curr_len += 1
            max_len = max(max_len, curr_len)
        else:
            curr_len = 1 

    return max_len

a = [6, 4, 9, 4, 7, 2, 3, 4, 2, 52]
print(longest_odd_even_subarray(a)) 
def kadane(a, n):
    max_sum = -99999999999999999999999999999
    cmax = 0

    for i in range(n):
        cmax = cmax + a[i]
        if cmax>max_sum:
            max_sum = cmax

        if cmax < 0:
            cmax = 0
    
    return max_sum

def circularSum(a, n):
    normal_max = kadane(a, n)
    total = 0
    for i in range(n):
        total += a[i]
    
    for i in range(n):
        a[i] = -a[i]
    
    min_subarray = kadane(a, n)

    for i in range(n):
        a[i] = -a[i]

    circular_max = total + min_subarray
    if circular_max == 0:
        return normal_max
    return max(normal_max, circular_max)

a = [1, -2, 3, -5, -4, 6]
print(circularSum(a, len(a)))
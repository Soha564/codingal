def MaxSubArraySum(a, a_size):
    max = -99999999999999999999999999999
    cmax = 0

    for i in range(0, a_size):
        cmax = cmax + a[i]
        if (max < cmax):
            max = cmax

        if cmax < 0:
            cmax = 0
    
    return max

a = [-12, -123, -213, -23, -33, -4, -24, -98, -1723897, -2112]
print(MaxSubArraySum(a, len(a)))
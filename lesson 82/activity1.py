def equillibrium(a):
    a_size = len(a)
    for i in range(a_size):
        right_sum  = 0
        left_sum = 0
        for j in range (0, i):
            left_sum += a[j]
        for k in range(i+1, a_size):
            right_sum += a[k]    
        if right_sum == left_sum:
            return i
    return -1
a = [1, 2, 3, 4, 6]
print(equillibrium(a))
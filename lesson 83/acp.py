def duplicate_check(a):
    a_size = len(a)
    for i in range(a_size):
        for j in range(i+1, a_size):
            if a[i] == a[j]:
                return j
    return -1
a = [1, 2, 3, 5, 6, 7, 2]
print(duplicate_check(a))

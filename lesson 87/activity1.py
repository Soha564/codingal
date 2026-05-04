def Order(a):
    a_size = len(a)
    for i in range(a_size):
        min_index = i
        minimum = 999999999999999999999999999999999999999999999
        for j in range(i, a_size):
            if a[j] < minimum:
                minimum = a[j]
                min_index = j
        a[i], a[min_index] = a[min_index], a[i]
    return a
a= [4, 3, 0, 1, 2]
print(Order(a))
        
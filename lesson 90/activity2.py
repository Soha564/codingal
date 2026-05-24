def intersection(a, b):
    c = []
    a_size = len(a)
    b_size = len(b)
    for i in range(a_size):
        for j in range(b_size):
                if a[i] == b[j]:
                    c.append(a[i])
    return c
a = [2, 3, 6, 5]
b = [7, 2, 6]
print(intersection(a, b))


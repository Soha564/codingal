def reverse_array(a):
    a_size = len(a)
    for i in range(a_size//2):
        num = a_size - i - 1
        a[i], a[num] = a[num], a[i]
    return a

a = [1, 2, 3, 4, 5]
print(reverse_array(a))
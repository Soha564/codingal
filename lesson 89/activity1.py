def Insertion_sort(a):
    a_size = len(a)
    for i in range(1, a_size):
        temp = a[i]
        j = i-1
        while j >=0 and temp <a[j]:
            a[j+1] = a[j]
            j -= 1
            a[j + 1] = temp
    return a

a = [10, 5, 11, 8, 2]
print(Insertion_sort(a))

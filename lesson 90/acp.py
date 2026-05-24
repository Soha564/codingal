def shell_sort(a):
    n = len(a)
    gap = n // 2 
    while gap > 0:
        for i in range(gap, n):
            temp = a[i]
            j = i
            while j >= gap and a[j - gap] > temp:
                a[j] = a[j - gap]
                j -= gap
            a[j] = temp
        gap //= 2  
    return a
a = []
a_size = int(input("Enter a size for the array: "))
for _ in range(a_size):
    a.append(int(input("Enter a number: ")))
print(shell_sort(a))
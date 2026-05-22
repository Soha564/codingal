def Insertion_sort(a):
    for i in range(1, a_size):
        temp = a[i]
        j = i-1
        while j >=0 and temp <a[j]:
            a[j+1] = a[j]
            j -= 1
            a[j + 1] = temp
    return a

a = []
a_size = int(input("Enter a size for the array:"))
for _ in range(a_size):
    print("Enter a number:")
    a.append(int(input()))
print(Insertion_sort(a))
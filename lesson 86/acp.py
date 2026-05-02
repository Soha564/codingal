def BubbleSort(a, a_size):
    for i in range(a_size):
        swap =  False
        for j in range(0, a_size - i - 1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swap = True
        if swap == False:
            break 
a = []
a_size = int(input("Enter size of array: "))
print("Start entering elements of array, each element in a new line:\n")
for k in range(a_size):
    b = int(input())
    a.append(b)                
BubbleSort(a, a_size)

print("\nSorted Array: ")
for i in range(len(a)):
    print("%d" %a[i], end = " ")
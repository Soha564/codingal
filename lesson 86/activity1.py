def BubbleSort(a):
    a_size = len(a)
    for i in range(a_size):
        swap =  False
        for j in range(0, a_size - i - 1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swap = True
        if swap == False:
            break 
a = [3, 4, 0, 2, 1]                
BubbleSort(a)

print("Sorted Array: ")
for i in range(len(a)):
    print("%d" %a[i], end = " ")
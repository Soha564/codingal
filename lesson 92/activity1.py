def Merge_sort(a):
    if len(a) > 1:
        mid = len(a)//2
        left = a[:mid]
        right = a[mid:]
        Merge_sort(left)
        Merge_sort(right)

        j = 0
        i = 0

        k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                a[k] = left[i]
                i += 1
            else:
                a[k] = right[j]
                j += 1

            k += 1

        while i < len(left):
            a[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            a[k] = right[j]
            j +=1
            k += 1
a = [59, 80, 38, 17, 90, 31, 56, 55, 21]
print("Unsorted Array: {}".format(a))
Merge_sort(a)
print("Sorted Array: {}". format(a))

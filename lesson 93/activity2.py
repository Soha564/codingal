def Merge_sort(a, b):
    i = j = 0
    k = 0

    merged = [0] * (len(a) + len(b))
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            merged[k] = a[i]
            i += 1
        else:
            merged[k] = b[j]
            j += 1
        k += 1

    while i < len(a):
        merged[k] = a[i]
        i += 1
        k += 1

    while j < len(b):
        merged[k] = b[j]
        j += 1
        k += 1
    
    final = []
    for num in merged:
        if not final or final[-1] != num:
            final.append(num)


    return final

a = [1, 3, 4, 7]
b = [2, 4, 5, 6]

print("Unsorted Arrays:", a, b)
result = Merge_sort(a, b)
print("Merged Sorted Array:", result)
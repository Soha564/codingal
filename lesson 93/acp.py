def Merge_sort(a, b):
    i = j = 0
    common = []

    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            common.append(a[i])
            i += 1
            j += 1
        elif a[i] < b[j]:
            i += 1
        else:
            j += 1

    return common

a = [1, 3, 4, 7]
b = [2, 4, 5, 6]

print("Unsorted Arrays:", a, b)
result = Merge_sort(a, b)
print("Numbers in both arrays:", result)


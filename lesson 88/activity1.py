from collections import Counter

arr = [4, 5, 6, 5, 4, 3]

freq = Counter(arr)
first_index = {}
for i in range(len(arr)):
    if arr[i] not in first_index:
        first_index[arr[i]] = i
arr.sort(key=lambda x: (-freq[x], first_index[x]))

print(arr)

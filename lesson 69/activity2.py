my_set = [1, 2, 3]

n = len(my_set)

for i in range(2 ** n):
    subset = []
    for j in range(n):
        if i & (1 << j):
            subset.append(my_set[j])
    print(subset)

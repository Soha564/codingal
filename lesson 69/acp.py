str = input("Enter a string: ")
set = []
n = len(str)
for i in str:
    set.append(i)

for i in range(2 ** n):
    subset = []
    for j in range(n):
        if i & (1 << j):
            subset.append(set[j])
    print(subset)

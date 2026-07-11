x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
col_sum = []
for j in range(len(x[0])):
    total = 0
    for i in range(len(x)):
        total += x[i][j]
    col_sum.append(total)
print(col_sum)
x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
row_sum = [[],[],[]]
for i in range(len(x)):
    total = 0
    for j in range(len(x[0])):
        total += x[i][j]
    row_sum[i] = total
print(row_sum)
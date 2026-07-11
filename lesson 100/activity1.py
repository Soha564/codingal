matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rows = len(matrix)
columns = len(matrix[0])
ans = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range(rows):
    for j in range(columns):
        ans[i][j] = matrix[j][i]
for _ in ans:
    print(_)
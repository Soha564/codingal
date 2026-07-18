matrix = [[1,2,3],[4,5,6],[7,8,9]]

rows = len(matrix)
cols = len(matrix[0])
ans = []
for j in range(cols):
    ans.append(matrix[0][j])
for i in range(1, rows):
    if matrix[i][0] not in ans:
        ans.append(matrix[i][0])
for _ in range(1, rows):
    if matrix[_][cols - 1] not in ans:
        ans.append(matrix[_][cols-1])
for k in range(cols):
    if matrix[rows - 1][k] not in ans:
        ans.append(matrix[rows-1][k])
print(ans)
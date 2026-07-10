x = [[8, 7], [2, 9]]
y = [[1, 2], [3, 4]]

answer = [[0,0], [0, 0]]

for i in range(len(x)):
    for j in range(len(x[0])):
        answer[i][j] = x[i][j] - y[i][j]

for r in answer:
    print(r)
    
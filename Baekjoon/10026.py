#적록색약 

import sys
sys.setrecursionlimit(10**6)

n = int(input())
data = []
for _ in range(n):
    tmp = input()
    row = []
    for x in tmp:
        row.append(x)
    data.append(row)
vertex = [[0 for _ in range(n)] for _ in range(n)]

def dfs(x, y):
    vertex[x][y] = 1
    if x < n - 1 and data[x + 1][y] == data[x][y] and vertex[x + 1][y] == 0:
        dfs(x + 1, y)
    if y < n - 1 and data[x][y + 1] == data[x][y] and vertex[x][y + 1] == 0:
        dfs(x, y + 1)
    if x > 0 and data[x - 1][y] == data[x][y] and vertex[x - 1][y] == 0:
        dfs(x - 1, y)
    if y > 0 and data[x][y - 1] == data[x][y] and vertex[x][y - 1] == 0:
        dfs(x, y - 1)

count1 = 0
for i in range(n):
    for j in range(n):
        if vertex[i][j] == 0:
            dfs(i, j)
            count1 += 1

for i in range(n):
    for j in range(n):
        if data[i][j] == "G":
            data[i][j] = "R"
vertex = [[0 for _ in range(n)] for _ in range(n)]

count2 = 0
for i in range(n):
    for j in range(n):
        if vertex[i][j] == 0:
            dfs(i, j)
            count2 += 1

print(count1, count2)


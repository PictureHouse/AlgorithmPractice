#음료수 얼려 먹기 

n, m = map(int, input().split())
ice = []
for _ in range(n):
    tmp = input()
    row = []
    for x in tmp:
        row.append(int(x))
    ice.append(row)

def dfs(x, y):
    ice[x][y] = 2
    if x > 0 and ice[x - 1][y] == 0:
        dfs(x - 1, y)
    if x < n - 1 and ice[x + 1][y] == 0:
        dfs(x + 1, y)
    if y > 0 and ice[x][y - 1] == 0:
        dfs(x, y - 1)
    if y < m - 1 and ice[x][y + 1] == 0:
        dfs(x, y + 1)

count = 0
for i in range(n):
    for j in range(m):
        if ice[i][j] == 0:
            dfs(i, j)
            count += 1
print(count)


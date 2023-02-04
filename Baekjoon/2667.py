#단지번호붙이기 

from collections import deque

n = int(input())
apart = []
for _ in range(n):
    tmp = input()
    row = []
    for x in tmp:
        row.append(int(x))
    apart.append(row)

def bfs(x, y, count):
    queue = deque()
    queue.append((x, y))
    apart[x][y] = 2
    count += 1
    while queue:
        x, y = queue.popleft()
        if x > 0 and apart[x - 1][y] == 1:
            queue.append((x - 1, y))
            apart[x - 1][y] = 2
            count += 1
        if y > 0 and apart[x][y - 1] == 1:
            queue.append((x, y - 1))
            apart[x][y - 1] = 2
            count += 1
        if x < n - 1 and apart[x + 1][y] == 1:
            queue.append((x + 1, y))
            apart[x + 1][y] = 2
            count += 1
        if y < n - 1 and apart[x][y + 1] == 1:
            queue.append((x, y + 1))
            apart[x][y + 1] = 2
            count += 1
    return count

num = 0
list = []
for i in range(n):
    for j in range(n):
        if apart[i][j] == 1:
            count = 0
            list.append(bfs(i, j, count))
            num += 1

print(num)
list.sort()
for x in list:
    print(x)


#미로 탐색 

from collections import deque
n, m = map(int, input().split())
maze= []
for _ in range(n):
    tmp = input()
    row = []
    for x in tmp:
        row.append(int(x))
    maze.append(row)

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        if x < n - 1 and maze[x + 1][y] == 1:
            queue.append((x + 1, y))
            maze[x + 1][y] = maze[x][y] + 1
        if y < m - 1 and maze[x][y + 1] == 1:
            queue.append((x, y + 1))
            maze[x][y + 1] = maze[x][y] + 1
        if x > 0 and maze[x - 1][y] == 1:
            if x - 1 != 0 or y != 0:
                queue.append((x - 1, y))
                maze[x - 1][y] = maze[x][y] + 1
        if y > 0 and maze[x][y - 1] == 1:
            if x != 0 or y - 1 != 0:
                queue.append((x, y - 1))
                maze[x][y - 1] = maze[x][y] + 1

count = 1
bfs(0, 0)
print(maze[n - 1][m - 1])


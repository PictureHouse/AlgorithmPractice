#DFS와 BFS 

import sys
sys.setrecursionlimit(10**6)
from collections import deque

n, m, v = map(int, input().split())
graph = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1
vertex = [0 for _ in range(n + 1)]

def dfs(v):
    vertex[v] = 1
    print(v, end = " ")
    for i in range(1, n + 1):
        if graph[v][i] == 1 and vertex[i] == 0:
            dfs(i)

def bfs(v):
    queue = deque()
    queue.append(v)
    vertex[v] = 1
    print(v, end = " ")
    while queue:
        u = queue.popleft()
        for w in range(1, n + 1):
            if graph[u][w] == 1 and vertex[w] == 0:
                queue.append(w)
                vertex[w] = 1
                print(w, end = " ")

dfs(v)
print()
vertex = [0 for _ in range(n + 1)]
bfs(v)


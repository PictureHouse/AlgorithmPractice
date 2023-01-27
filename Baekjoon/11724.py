#연결 요소의 개수 

import sys
sys.setrecursionlimit(10**6)

n, m = map(int, sys.stdin.readline().rstrip().split())
vertex = [0 for _ in range(n + 1)]
graph = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, sys.stdin.readline().rstrip().split())
    graph[u][v] = 1
    graph[v][u] = 1

def dfs(graph, v):
    vertex[v] = 1
    for i in range(n + 1):
        if graph[v][i] == 1 and vertex[i] == 0:
            dfs(graph, i)

count = 0
for i in range(1, n + 1):
    if vertex[i] == 0:
        dfs(graph, i)
        count += 1
print(count)


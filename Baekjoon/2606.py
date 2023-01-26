#바이러스 

n = int(input())
computer = [0 for _ in range(n + 1)]
network = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
connect = int(input())
for i in range(connect):
    a, b = map(int, input().split())
    network[a][b] = 1
    network[b][a] = 1

def dfs(network, v, computer):
    computer[v] = 1
    for i in range(n + 1):
        if network[v][i] == 1 and computer[i] == 0:
            dfs(network, i, computer)

dfs(network, 1, computer)
print(sum(computer) - 1)


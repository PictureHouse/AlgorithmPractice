#빗물 

h, w = map(int, input().split())
data = list(map(int, input().split()))
world_map = [[0] * w for _ in range(h)]
for i in range(h):
    for j in range(w):
        if data[j] >= h - i:
            world_map[i][j] = 1

count = 0
for i in range(h):
    flag = 0
    tmp = 0
    for j in range(w):
        if flag == 0 and world_map[i][j] == 1:
            flag = 1
        elif flag == 1 and world_map[i][j] == 1:
            count += tmp
            tmp = 0
        elif flag == 1 and world_map[i][j] == 0:
            tmp += 1
print(count)


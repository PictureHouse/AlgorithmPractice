#소가 길을 건너간 이유3

n = int(input())
cow = []
for i in range(n):
    cow.append(tuple(map(int, input().split())))

cow.sort()
time = 0
for i in range(n):
    if cow[i][0] > time:
        time += (cow[i][0] - time)
    time += cow[i][1]
print(time)


#Project Teams

n = int(input())
data = list(map(int, input().split()))

data.sort()
min = 1e9
for i in range(n):
    if data[i] + data[-i - 1] < min:
        min = data[i] + data[-i - 1]
print(min)


#센서 

n = int(input())
k = int(input())
sensor = list(map(int, input().split()))

sensor.sort()
diff = []
for i in range(n - 1):
    diff.append(sensor[i + 1] - sensor[i])
diff.sort()

sum = 0
for i in range(len(diff) - (k - 1)):
    sum += diff[i]
print(sum)


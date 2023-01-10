#행복 유치원 

n, k = map(int, input().split())
height = list(map(int, input().split()))

diff = []
for i in range(1, n):
    diff.append(height[i] - height[i - 1])
diff.sort()
cost = 0
for i in range((n - 1) - (k - 1)):
    cost += diff[i]
print(cost)


#떡볶이 떡 만들기 

n, m = map(int, input().split())
height = list(map(int, input().split()))

sum = 0
while sum < m:
    longest = max(height)
    cut = longest - 1
    for i in range(n):
        if height[i] > cut:
            height[i] -= 1
            sum += 1
print(cut)


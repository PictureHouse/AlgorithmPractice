#가장 긴 증가하는 부분 수열 

n = int(input())
a = list(map(int, input().split()))

result = [0 for _ in range(n)]
for i in range(n):
    for j in range(i):
        if a[i] > a[j] and result[i] < result[j]:
            result[i] = result[j]
    result[i] += 1
print(max(result))


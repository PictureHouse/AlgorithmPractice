#큰 수의 법칙 

n, m, k = map(int, input().split())
num = list(map(int, input().split()))

num.sort(reverse = True)
result = 0
count = 0
index = 0
while index < m:
    if count < k - 1:
        result += num[0]
        count += 1
    elif count == k - 1:
        result += num[1]
        count = 0
    index += 1
print(result)


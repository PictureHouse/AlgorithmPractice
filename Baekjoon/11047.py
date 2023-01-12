#동전0 

n, k = map(int, input().split())
coin = []
for i in range(n):
    coin.append(int(input()))

coin.sort(reverse = True)
count = 0
for x in coin:
    if k == 0:
        break
    else:
        if x <= k:
            count += k // x
            k = k % x
print(count)


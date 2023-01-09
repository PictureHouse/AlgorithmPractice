#거스름돈 

n = int(input())
count = 0

if n == 1 or n == 3:
    print(-1)
else:
    coin = 5
    count += n // coin
    if (n % coin) % 2 != 0:
        count -= 1
        n = (n % coin) + coin
    else:
        n = n % coin

    coin = 2
    count += n // coin
    n = n % coin

    print(count)


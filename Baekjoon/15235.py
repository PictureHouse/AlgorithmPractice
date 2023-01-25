#Olympiad Pizza 

n = int(input())
num = list(map(int, input().split()))

time = 0
times = [0 for _ in range(n)]
index = 0
while sum(num) != 0:
    if num[index] != 0:
        time += 1
        num[index] -= 1
        times[index] = time
    if index == n - 1:
        index = 0
    else:
        index += 1
for t in times:
    print(t, end = " ")


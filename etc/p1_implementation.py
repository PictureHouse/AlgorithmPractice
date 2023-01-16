#상하좌우 

n = int(input())
move = list(map(str, input().split()))

now = [1, 1]
for x in move:
    if x == "L":
        if now[1] > 1:
            now[1] -= 1
    elif x == "R":
        if now[1] < n - 1:
            now[1] += 1
    elif x == "U":
        if now[0] > 1:
            now[0] -= 1
    elif x == "D":
        if now[0] < n - 1:
            now[0] += 1
print(f"{now[0]} {now[1]}")


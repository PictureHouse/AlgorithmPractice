#로봇 청소기 

n, m = map(int, input().split())
r, c, d = map(int, input().split())
room = []
for i in range(n):
    room.append(list(map(int, input().split())))

count = 0
turn = 0
while True:
    if room[r][c] == 0:
        room[r][c] = 2
        count += 1

    if d == 0:
        if room[r][c - 1] == 0:
            d = 3
            c -= 1
            turn = 0
        elif turn == 4:
            if room[r + 1][c] == 1:
                break
            else:
                r += 1
                turn = 0
        else:
            d = 3
            turn += 1
    elif d == 1:
        if room[r - 1][c] == 0:
            d = 0
            r -= 1
            turn = 0
        elif turn == 4:
            if room[r][c - 1] == 1:
                break
            else:
                c -= 1
                turn = 0
        else:
            d = 0
            turn += 1
    elif d == 2:
        if room[r][c + 1] == 0:
            d = 1
            c += 1
            turn = 0
        elif turn == 4:
            if room[r - 1][c] == 1:
                break
            else:
                r -= 1
                turn = 0
        else:
            d = 1
            turn += 1
    elif d == 3:
        if room[r + 1][c] == 0:
            d = 2
            r += 1
            turn = 0
        elif turn == 4:
            if room[r][c + 1] == 1:
                break
            else:
                c += 1
                turn = 0
        else:
            d = 2
            turn += 1
print(count)


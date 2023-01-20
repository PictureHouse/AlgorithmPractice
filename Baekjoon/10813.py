#공 바꾸기 

n, m = map(int, input().split())
ball = []
for i in range(n):
    ball.append(i + 1)
data = []
for i in range(m):
    data.append(tuple(map(int, input().split())))

for i in range(m):
    tmp = ball[data[i][0] - 1]
    ball[data[i][0] - 1] = ball[data[i][1] - 1]
    ball[data[i][1] - 1] = tmp

for i in range(n):
    print(ball[i], end = " ")


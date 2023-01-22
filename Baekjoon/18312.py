#시각 

n, k = map(int, input().split())

count = 0
for h in range(n + 1):
    for m in range(60):
        for s in range(60):
            if h < 10:
                time = "0" + str(h) + "시"
            else:
                time = str(h) + "시"
            if m < 10:
                time += "0" + str(m) + "분"
            else:
                time += str(m) + "분"
            if s < 10:
                time += "0" + str(s) + "초"
            else:
                time += str(s) + "초"

            if str(k) in time:
                count += 1

print(count)


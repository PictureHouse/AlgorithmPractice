#시각 

n = int(input())

count = 0
for h in range(n + 1):
    for m in range(60):
        for s in range(60):
            time = str(h) + "시" + str(m) + "분" + str(s) + "초"
            if "3" in time:
                count += 1
print(count)


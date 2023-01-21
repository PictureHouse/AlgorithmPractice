#기상캐스터 

h, w = map(int, input().split())
cloud = []
for i in range(h):
    cloud.append(input())

for i in range(h):
    flag = 0
    count = 0
    for x in cloud[i]:
        if x == "c":
            print(0, end = " ")
            flag = 1
            count = 0
        elif x == "." and flag == 0:
            print(-1, end = " ")
        elif x == "." and flag == 1:
            count += 1
            print(count, end = " ")
    print()


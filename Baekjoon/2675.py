#문자열 반복 

t = int(input())
case = []
for i in range(t):
    case.append(list(map(str, input().split())))

for i in range(t):
    num = int(case[i][0])
    for x in case[i][1]:
        print(x * num, end = "")
    print()


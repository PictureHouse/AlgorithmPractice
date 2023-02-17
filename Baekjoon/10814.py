#나이순 정렬 

n = int(input())
member = []
for _ in range(n):
    tmp = list(map(str, input().split()))
    member.append((int(tmp[0]), tmp[1]))

member.sort(key = lambda member: member[0])
for x in member:
    print(x[0], x[1])


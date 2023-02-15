#위에서 아래로 

n = int(input())
num = []
for _ in range(n):
    num.append(int(input()))

num.sort(reverse=True)
for x in num:
    print(x, end = " ")


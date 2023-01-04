#배열 합치기 

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.extend(b)
a.sort()
for x in a:
    print(x, end = " ")


#스네이크버드 

n, l = map(int, input().split())
fruits = list(map(int, input().split()))

fruits.sort()
for x in fruits:
    if x <= l:
        l += 1
print(l)


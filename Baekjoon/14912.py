#숫자 빈도수 
    
n, d = map(int, input().split())

list = []
for i in range(1, n + 1):
    list.append(str(i))

count = 0
for x in list:
    count += x.count(str(d))
print(count)


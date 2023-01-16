#등수 매기기 

n = int(input())
data = []
for i in range(n):
    data.append(int(input()))

data.sort()
result = 0
for i in range(n):
    result += abs(data[i] - (i + 1))
print(result)


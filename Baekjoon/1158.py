#요세푸스 문제 

n, k = map(int, input().split())
people = []
for i in range(1, n + 1):
    people.append(i)

result = []
index = 0
count = 1
while len(people) != 0:
    if count == k:
        result.append(people[index])
        if index == len(people) - 1:
            people.remove(people[index])
            index = 0
        else:
            people.remove(people[index])
        count = 1
    elif index == len(people) - 1:
        count += 1
        index = 0
    else:
        count += 1
        index += 1

print("<", end = "")
for i in range(n):
    if i == n - 1:
        print(result[i], end = "")
    else:
        print(result[i], end = ", ")
print(">")


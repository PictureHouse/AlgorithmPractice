#도서관 
   
n, m = map(int, input().split())
location = list(map(int, input().split()))

neg = []
pos = []
for l in location:
    if l < 0:
        neg.append(l)
    else:
        pos.append(l)
neg.sort()
pos.sort(reverse = True)

steps = []
count = 0
for x in neg:
    if m == 1:
        steps.append(abs(x))
    else:
        if count == 0:
            steps.append(abs(x))
            count += 1
        elif count == m - 1:
            count = 0
        else:
            count += 1
count = 0
for y in pos:
    if m == 1:
        steps.append(y)
    else:
        if count == 0:
            steps.append(y)
            count += 1
        elif count == m - 1:
            count = 0
        else:
            count += 1
steps.sort(reverse = True)
min_steps = 0
for i in range(1, len(steps)):
    min_steps += 2 * steps[i]
min_steps += steps[0]
print(min_steps)


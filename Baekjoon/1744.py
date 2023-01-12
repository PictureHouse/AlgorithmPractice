#수 묶기 

n = int(input())
pos = []
neg = []
for i in range(n):
    tmp = int(input())
    if tmp >= 0:
        pos.append(tmp)
    else:
        neg.append(tmp)

pos.sort(reverse = True)
neg.sort()
num = pos + neg

new = []
i = 0
while i < len(num):
    if i == len(num) - 1:
        new.append(num[i])
        i += 1
    elif num[i] == 0 and num[i + 1] < 0 and (len(num) - i) % 2 != 0:
        new.append(num[i])
        i += 1
    elif num[i] == 0 and num[i + 1] < 0 and (len(num) - i) % 2 == 0:
        new.append(num[i] * num[len(num) - 1])
        num.remove(num[len(num) - 1])
        i += 1
    else:
        if num[i] * num[i + 1] > num[i] + num[i + 1]:
            new.append(num[i] * num[i + 1])
            i += 2
        else:
            new.append(num[i])
            i += 1
print(sum(new))


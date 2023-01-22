#왕실의 나이트 

point = input()
h = point[0]
v = point[1]

count = 0
if h >= "c":
    if int(v) > 2:
        count += 2
    elif int(v) == 2:
        count += 1
    if int(v) < 7:
        count += 2
    elif int(v) == 7:
        count += 1
if h <= "f":
    if int(v) > 2:
        count += 2
    elif int(v) == 2:
        count += 1
    if int(v) < 7:
        count += 2
    elif int(v) == 7:
        count += 1
print(count)


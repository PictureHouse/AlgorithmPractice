#UCPC는 무엇의 약자일까?

input = input()

flag1 = 0
flag2 = 0
flag3 = 0
flag4 = 0
for x in input:
    if flag1 == 0:
        if x == "U":
            flag1 = 1
    elif flag2 == 0:
        if x == "C":
            flag2 = 1
    elif flag3 == 0:
        if x  == "P":
            flag3 = 1
    elif flag4 == 0:
        if x == "C":
            flag4 = 1

if flag1 * flag2 * flag3 * flag4 == 1:
    print("I love UCPC")
else:
    print("I hate UCPC")


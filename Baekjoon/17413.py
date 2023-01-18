#단어 뒤집기2

s = input()

result = ""
tmp = ""
flag = 0
for x in s:
    if x == "<":
        i = len(tmp) - 1
        while i >= 0:
            result += tmp[i]
            i -= 1
        tmp = x
        flag = 1
    elif flag == 1 and x == ">":
        tmp += x
        result += tmp
        tmp = ""
        flag = 0
    elif flag == 0 and x == " ":
        i = len(tmp) - 1
        while i >= 0:
            result += tmp[i]
            i -= 1
        result += " "
        tmp = ""
    else:
        tmp += x
if tmp != "":
    i = len(tmp) - 1
    while i >= 0:
        result += tmp[i]
        i -= 1
print(result)


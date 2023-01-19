#단어 뒤집기 

t = int(input())
data = []
for i in range(t):
    data.append(input())

for i in range(t):
    tmp = ""
    result = ""
    for x in data[i]:
        if x == " ":
            for j in range(len(tmp)):
                result += tmp[len(tmp) - j - 1]
            tmp = ""
            result += " "
        else:
            tmp += x
    if tmp != "":
        for j in range(len(tmp)):
                result += tmp[len(tmp) - j - 1]
    print(result)


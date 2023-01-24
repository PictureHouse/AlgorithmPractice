#괄호 

t = int(input())
data = []
for _ in range(t):
    data.append(input())

for ps in data:
    stack = []
    flag = 0
    for x in ps:
        if x == "(":
            stack.append("(")
        elif x == ")" and len(stack) != 0:
            stack.pop()
        elif x == ")" and len(stack) == 0:
            flag = 1
            break
    if flag == 0 and len(stack) == 0:
        print("YES")
    else:
        print("NO")


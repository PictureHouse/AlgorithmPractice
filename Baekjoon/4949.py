#균형잡힌 세상 

data = []
while True:
    string = input()
    if string == ".":
        break
    data.append(string)

for string in data:
    stack = []
    flag = 0
    for x in string:
        if x == "(" or x == "[":
            stack.append(x)
        elif x == ")" and len(stack) != 0:
            if stack.pop() != "(":
                flag = 1
                break
        elif x == ")" and len(stack) == 0:
            flag = 1
            break
        elif x == "]" and len(stack) != 0:
            if stack.pop() != "[":
                flag = 1
                break
        elif x == "]" and len(stack) == 0:
            flag = 1
            break
    if len(stack) == 0 and flag == 0:
        print("yes")
    else:
        print("no")


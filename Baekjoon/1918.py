#후위 표기식 

infix = input()

postfix = ""
stack = []
for x in infix:
    if x == "(":
        stack.append(x)
    elif x in ("*", "/"):
        while len(stack) != 0 and stack[-1] in ("*", "/"):
            postfix += stack.pop()
        stack.append(x)
    elif x in ("+", "-"):
        while len(stack) != 0 and stack[-1] in ("*", "/", "+", "-"):
            postfix += stack.pop()
        stack.append(x)
    elif x == ")":
        while stack[-1] != "(":
            postfix += stack.pop()
        stack.pop()
    else:
        postfix += x
while len(stack) != 0:
    postfix += stack.pop()
print(postfix)


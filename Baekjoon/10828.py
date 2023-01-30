#스택 

import sys
n = int(sys.stdin.readline().rstrip())
stack = []
command = []
result = []
for _ in range(n):
    command = list(map(str, sys.stdin.readline().rstrip().split()))
    if command[0] == "push":
        stack.append(int(command[1]))
    elif command[0] == "pop":
        if len(stack) == 0:
            result.append(-1)
        else:
            result.append(stack.pop())
    elif command[0] == "size":
        result.append(len(stack))
    elif command[0] == "empty":
        if len(stack) == 0:
            result.append(1)
        else:
            result.append(0)
    elif command[0] == "top":
        if len(stack) == 0:
            result.append(-1)
        else:
            result.append(stack[-1])
    command.clear

for x in result:
    print(x)


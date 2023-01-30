#큐2 

import sys
from collections import deque
n = int(sys.stdin.readline().rstrip())
queue = deque()
command = []
result = []
for _ in range(n):
    command = list(map(str, sys.stdin.readline().rstrip().split()))
    if command[0] == "push":
        queue.append(int(command[1]))
    elif command[0] == "pop":
        if len(queue) == 0:
            result.append(-1)
        else:
            result.append(queue.popleft())
    elif command[0] == "size":
        result.append(len(queue))
    elif command[0] == "empty":
        if len(queue) == 0:
            result.append(1)
        else:
            result.append(0)
    elif command[0] == "front":
        if len(queue) == 0:
            result.append(-1)
        else:
            result.append(queue[0])
    elif command[0] == "back":
        if len(queue) == 0:
            result.append(-1)
        else:
            result.append(queue[-1])
    command.clear

for x in result:
    print(x)


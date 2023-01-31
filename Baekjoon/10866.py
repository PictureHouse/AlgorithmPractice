#덱 

import sys
from collections import deque
n = int(sys.stdin.readline().rstrip())
deq = deque()
command = []
result = []
for _ in range(n):
    command = list(map(str, sys.stdin.readline().rstrip().split()))
    if command[0] == "push_front":
        deq.appendleft(int(command[1]))
    elif command[0] == "push_back":
        deq.append(int(command[1]))
    elif command[0] == "pop_front":
        if len(deq) == 0:
            result.append(-1)
        else:
            result.append(deq.popleft())
    elif command[0] == "pop_back":
        if len(deq) == 0:
            result.append(-1)
        else:
            result.append(deq.pop())
    elif command[0] == "size":
        result.append(len(deq))
    elif command[0] == "empty":
        if len(deq) == 0:
            result.append(1)
        else:
            result.append(0)
    elif command[0] == "front":
        if len(deq) == 0:
            result.append(-1)
        else:
            result.append(deq[0])
    elif command[0] == "back":
        if len(deq) == 0:
            result.append(-1)
        else:
            result.append(deq[-1])
    command.clear

for x in result:
    print(x)


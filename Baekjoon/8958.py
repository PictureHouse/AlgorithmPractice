#OX퀴즈 

import sys
n = int(input())
input = []
for x in range(n):
    input.append(sys.stdin.readline().rstrip())

for x in input:
    score = 0
    count = 0
    for y in x:
        if y == "O":
            count += 1
            score += count
        else:
            count = 0
    print(score)


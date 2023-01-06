#차집합 

import sys
a_num, b_num = map(int, input().split())
a = set(map(int, sys.stdin.readline().rstrip().split()))
b = set(map(int, sys.stdin.readline().rstrip().split()))

result = a - b
result = list(result)
print(len(result))
if len(result) != 0:
    result.sort()
    for x in result:
        print(x, end = " ")


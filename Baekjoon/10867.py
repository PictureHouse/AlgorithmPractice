#중복 빼고 정렬하기

import sys
n = int(input())
nums = set(map(int, sys.stdin.readline().rstrip().split()))
result = list(nums)
result.sort()
for x in result:
    print(x, end = " ")


#숫자 카드 

import sys
n = int(input())
a = set(map(int, sys.stdin.readline().rstrip().split()))
m = int(input())
list = list(map(int, sys.stdin.readline().rstrip().split()))

for x in list:
    if x in a:
        print(1, end = " ")
    else:
        print(0, end = " ")


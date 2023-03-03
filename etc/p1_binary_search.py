#부품 찾기 

n = int(input())
parts = list(map(int, input().split()))
m = int(input())
request = list(map(int, input().split()))

def binary_search(array, target, start, end):
    if start > end:
        return -1
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)

parts.sort()
for x in request:
    result = binary_search(parts, x, 0, n - 1)
    if result == -1:
        print("no", end = " ")
    else:
        print("yes", end = " ")


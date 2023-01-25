#좋은 단어 

n = int(input())
word = []
for i in range(n):
    word.append(input())

count = 0
for w in word:
    stack = []
    for x in w:
        if len(stack) != 0 and x == stack[-1]:
            stack.pop()
        else:
            stack.append(x)
    if len(stack) == 0:
        count += 1
print(count)


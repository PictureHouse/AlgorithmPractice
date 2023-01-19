#팰린드롬인지 확인하기 

word = input()

flag = 1
for i in range(len(word) // 2):
    if word[i] != word[-1 - i]:
        flag = 0
        break
print(flag)


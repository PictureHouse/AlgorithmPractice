#뒤집기 

s = input()

count = 0
tmp = s[0]
for i in range(1, len(s)):
    if tmp != s[i]:
        count += 1
    tmp = s[i]
if count % 2 == 0:
    result = count // 2
else:
    result = count // 2 + 1
print(result)


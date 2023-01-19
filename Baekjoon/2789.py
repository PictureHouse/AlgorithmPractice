#유학 금지

word = input()

result = ""
for x in word:
    if x not in "CAMBRIDGE":
        result += x
print(result)


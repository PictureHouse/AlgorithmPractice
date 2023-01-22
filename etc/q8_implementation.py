#문자열 재정렬 

data = input()

alphabet = []
sum = 0
for x in data:
    if x.isnumeric():
       sum += int(x)
    else:
        alphabet.append(x)
alphabet.sort()
result = ""
for x in alphabet:
    result += x
result += str(sum)
print(result)


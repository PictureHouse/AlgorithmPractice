#팰린드롬수 

num = []
tmp = input()
while tmp != "0":
    num.append(tmp)
    tmp = input()

for x in num:
    flag = 0
    for i in range(len(x) // 2):
        if x[i] != x[-1 - i]:
            flag = 1
            print("no")
            break
    if flag == 0:
        print("yes")


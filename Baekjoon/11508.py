#2+1 세일 

n = int(input())
price = []
for i in range(n):
    price.append(int(input()))

price.sort(reverse = True)
min_price = 0
count = 0
for i in range(n):
    if count == 0 or count == 1:
        min_price += price[i]
        count += 1
    elif count == 2:
        min_price += 0
        count = 0
print(min_price)


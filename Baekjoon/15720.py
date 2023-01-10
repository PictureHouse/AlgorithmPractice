#카우버거 

h, s, d = map(int, input().split())
hamburger = list(map(int, input().split()))
side = list(map(int, input().split()))
drink = list(map(int, input().split()))

num_of_set = min(h, s, d)
hamburger.sort(reverse = True)
side.sort(reverse = True)
drink.sort(reverse = True)

total = 0
sale = 0
for i in range(h):
    total += hamburger[i]
    if i < num_of_set:
        sale += hamburger[i] * 0.9
    else:
        sale += hamburger[i]
for i in range(s):
    total += side[i]
    if i < num_of_set:
        sale += side[i] * 0.9
    else:
        sale += side[i]
for i in range(d):
    total += drink[i]
    if i < num_of_set:
        sale += drink[i] * 0.9
    else:
        sale += drink[i]
print(total)
print(int(sale))


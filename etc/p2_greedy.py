#숫자 카드 게임 

n, m = map(int, input().split())
card = []
for i in range(n):
    card.append(list(map(int, input().split())))

min_card = []
for i in range(n):
    min_card.append(min(card[i]))
print(max(min_card))


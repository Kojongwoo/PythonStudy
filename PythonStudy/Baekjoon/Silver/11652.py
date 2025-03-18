N = int(input())  
cards = {}  

for _ in range(N):
    card = int(input())
    if card in cards:     
        cards[card] += 1  
    else:                 
        cards[card] = 1   

max_count = 0
min_card = 0

for card, count in cards.items():
    if count > max_count or (count == max_count and card < min_card):
        max_count = count
        min_card = card

print(min_card)

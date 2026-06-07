import art
import random
print(art.logo)
dealer_cards = []
user_cards = []
dealer_sum = 0
user_sum = 0

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def start_deal():
    for i in range(2):
        dealer_cards.append(random.choice(cards))
        user_cards.append(random.choice(cards))
    print(f"[{dealer_cards[0]},X]")
    print(user_cards)

stand = False
def check():
    while not stand
for i in dealer_cards
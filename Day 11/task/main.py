from os import remove

import art
import random
print(art.logo)


#
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# def start_deal():
#     for i in range(2):
#         dealer_cards.append(random.choice(cards))
#         user_cards.append(random.choice(cards))
#     print(f"[{dealer_cards[0]},X]")
#     print(user_cards)
#
#
# def check_cards():
#     dealer_sum = check_sum(dealer_cards)
#     user_sum = check_sum(user_cards)
#     if dealer_sum == 21:
#         if user_sum == 21:
#             print("push")
#         else:
#             print("Black Jack for House")
#     elif user_sum == 21:
#         if dealer_sum == 21:
#             print("push")
#         else:
#             print("Black Jack!")
#     elif user_sum > 21:
#         print("Bust")
#     elif dealer_sum > 21:
#         print("House Lost")
#
# def user_turn():
#     over_21 = False
#     while not over_21:
#         user_choice = input("Do you want to stand or hit, type: ").lower()
#         if user_choice == "stand":
#             print("\n")
#             break
#         elif user_choice == "hit":
#             user_cards.append(random.choice(cards))
#             print(f"{user_cards} current score : {check_sum(user_cards)})
#             if check_sum(user_cards) > 21:
#                 print("Bust")
#                 over_21 = True
#
# def dealer_turn():
#     over_17 = False
#     while not over_17:
#         if check_sum(dealer_cards) < 17:
#             dealer_cards.append(random.choice(cards))
#             if check_sum(dealer_cards) > 21:
#                 print("Bust")
#             elif check_sum(dealer_cards) > 17:
#                 over_17 = True
#                 if check_sum(dealer_cards) > check_sum(user_cards):
#                     print("HOuse Wins")
#         else:
#             over_17 = True
#
#
#
# def check_sum(check_card):
#     checked_card = sum(check_card)
#     return checked_card
#
# def compare(dealer_card,user_card):
#     if check_sum(dealer_card) > check_sum(user_card) and check_sum(dealer_card)<=21:
#         print("HOUSE WINS")
#     elif check_sum(user_card) > check_sum(dealer_card) and check_sum(user_card)<=21:
#         print("Round Won!")
#
# start_deal()
#
# print(check_sum(user_cards))
# print(check_sum(dealer_cards))
#
# user_turn()
#
# print(user_cards)
# print(check_sum(user_cards))

dealer_cards = []
user_cards = []

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    elif sum(cards)>21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

for _ in range(2):
    user_cards.append(deal_card())
    dealer_cards.append(deal_card())

user_score = calculate_score(user_cards)
dealer_score = calculate_score(dealer_cards)


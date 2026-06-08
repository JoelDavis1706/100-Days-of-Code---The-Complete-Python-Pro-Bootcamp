import art
import random
print(art.logo)

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def compare_score(u_score, d_score):

    if u_score == d_score:
        return "DRAW"
    elif d_score == 0:
        return "Lose, opponent has BlackJack!"
    elif u_score == 0:
        return "User won by BlackJack!"
    elif u_score > 21:
        return "User lost by Bust!"
    elif d_score > 21:
        return "House lost by Bust!"
    elif u_score > d_score:
        return "You Win!"
    else:
        return "You Lose"


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    elif sum(cards)>21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def play_game():
    dealer_cards = []
    user_cards = []
    dealer_score = -1
    user_score = -1
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        dealer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        dealer_score = calculate_score(dealer_cards)
        print(f"Dealer Cards [{dealer_cards[0]},X] , Dealer Score: {dealer_score}")
        print(f"User Cards {user_cards} , User Score: {user_score}")

        if user_score == 0 or dealer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Enter y to hit or n to stand: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while dealer_score!=0 and dealer_score<17:
        dealer_cards.append(deal_card())
        dealer_score = calculate_score(dealer_cards)

    print(f"Dealer Final Cards [{dealer_cards[0]},X] , Dealer Final Score: {dealer_score}")
    print(f"Your Final Cards {user_cards} , Your Final Score: {user_score}")
    print(compare_score(user_score,dealer_score))
play_game()

while input("Do you want to play ? :").lower() == "y":
    print("\n" * 50)
    play_game()
# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
import art
print(art.logo)

dictionary = {}
game_over = False


def highest_bidder(bidding_dictionary):
    max = 0
    for user in bidding_dictionary:
        if bidding_dictionary[user] > max:
            max = bidding_dictionary[user]
            max_bidder = user
    print(f"The bid winner is {max_bidder} with a bid of {max}")



while game_over is not True:
    name = input("Enter your Name:")
    bid = int(input("Enter your bid:"))
    dictionary[name] = bid
    decision = input("Are there new bids to be added type 'yes' or 'no':").lower()

    if decision == "yes":
        print("\n" * 100)
    elif decision == "no":
        game_over = True
        highest_bidder(dictionary)


#Display Art
import random
import art
import game_data
print(art.logo)

#generate random data from dictionary
def gen_ran():
    random_option = random.choice(game_data.data)
    return random_option

#Format the account into printable format
def format():
    random_A = gen_ran()
    random_B = gen_ran()
    print(f"Compare A:{random_A['name']}, a {random_A['description']}, from {random_A['country']}")
    print(art.vs)
    print(f"Against B:{random_B['name']}, a {random_B['description']}, from {random_B['country']}")

#Ask user for a guess
def ask_guess():


#Check if user is correct

## - Check follower count of each account

## - Use if statement to check if user is correct


#Give user feedback on their guess

#Keeping the score

#make the game repeatable.

#make the account at position at B become the next A



# game_over = False
# while game_over not True:
#     print(game_data[])
format()
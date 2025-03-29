# This is the higher and lower game
import random
from resource.higher_lower import logo, vs # getting the art
from resource.higher_lower_game_data import data # getting the data from a list

# function to choose a random person
def choose_person(data:list):
        return random.choice(data)

def show_person_1():
    print(f"Compare A: {person_1['name']}, a {person_1['description']}, from {person_1['country']}")

def show_person_2():
    print(f"Compare B: {person_2['name']}, a {person_2['description']}, from {person_2['country']}")
def show_comparison():
    # Starts console display
    print(logo)    
    # print A
    show_person_1()
    print(vs)
    # print B
    show_person_2()
    print(f"Current Score is {score}")
    # for dev
    print(person_1['follower_count'])
    print(person_2['follower_count'])
    # ask user to make a choice

# score integer to track the scores
score = 0
# game switch for while loop
game_continue = True
# Initialise candidates
person_1 = choose_person(data)
person_2 = choose_person(data)


while game_continue:
# display the comparison
    show_comparison()
    # ask for input
    choice = (input(f"Who has more followers? 'A' or 'B': ")).lower()

# make decision compare person 1 and 2 ['follower_count']

# user choose a and A is higher than B
    if choice == 'a' and person_1['follower_count'] > person_2['follower_count']:
        # score increases by 1, chose a new person B
        score += 1
        print(f"You are correct! Score = {score}")
        person_2 = choose_person(data)
        show_comparison()
    # user choose b and A is lower than B
    elif choice == 'b' and person_1['follower_count'] < person_2['follower_count']:
        score += 1
        print(f"You are correct! Score = {score}")
        person_1 = person_2
        person_2 = choose_person(data)
        show_comparison()
    else: # all the lose conditions will end the game
        print(f"""
        {person_2['name']} has {person_2['follower_count']} followers while
        {person_1['name']} has {person_1['follower_count']}, you lose!
        your final score is {score}!
        """)
        game_continue = False
          
          
## improved codebase (with guidance by AI)
# # This is the higher and lower game
# import random
# from resource.higher_lower import logo, vs  # getting the art
# from resource.higher_lower_game_data import data  # getting the data from a list

# def choose_person(data_list):
#     """Return a random account from data."""
#     return random.choice(data_list)

# def format_data(account):
#     """Format account data into printable format."""
#     name = account["name"]
#     description = account["description"]
#     country = account["country"]
#     return f"{name}, a {description}, from {country}"

# def check_answer(guess, a_followers, b_followers):
#     """Check if user's guess is correct and return a boolean."""
#     if a_followers > b_followers:
#         return guess == 'a'
#     else:
#         return guess == 'b'

# def game():
#     """Main game function that contains the gameplay loop."""
#     print(logo)
#     score = 0
#     game_continue = True
#     # Initial selection
#     person_a = choose_person(data)
#     person_b = choose_person(data)
    
#     while game_continue:
#         # Make sure we don't compare the same account
#         while person_a == person_b:
#             person_b = choose_person(data)
            
#         # Display the comparison
#         print(logo)  
#         print(f"Compare A: {format_data(person_a)}")
#         print(vs)
#         print(f"Compare B: {format_data(person_b)}")
#         print(f"Current Score: {score}")
        
#         # Get user input
#         choice = input("Who has more followers? 'A' or 'B': ").lower()
        
#         # Get follower counts
#         a_followers = person_a["follower_count"]
#         b_followers = person_b["follower_count"]
        
#         # Check answer
#         if check_answer(choice, a_followers, b_followers):
#             score += 1
#             print(f"You are correct! Score = {score}")
#             # Make B become the new A, and get a new B
#             person_a = person_b
#             person_b = choose_person(data)
#         else:
#             print(f"""
#             {person_b['name']} has {b_followers} followers while
#             {person_a['name']} has {a_followers} followers, you lose!
#             Your final score is {score}!
#             """)
#             game_continue = False

# This line is special. when the script is called directly 
# python will set variable "__name__" as string "__main__"
# This means to run the game function only when it is called directly.

# if __name__ == "__main__":
#     game()        
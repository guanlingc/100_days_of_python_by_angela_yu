# This is the higher and lower game
import random
from resource.higher_lower import logo, vs # getting the art
from resource.higher_lower_game_data import data # getting the data from a list

# function to choose a random person
def choose_person(data:list):
    # randint uses literal number and zero index ( so index 0 to index 49)
    # len(data) = 50, so subtract 1 from it
    random_index = random.randint(0,(len(data)-1))
    return data[random_index]

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
          
          
        
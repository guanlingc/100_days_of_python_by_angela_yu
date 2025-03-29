# Goal is to make a number guessing game 
import random

def set_difficulty(difficulty:str):
    # set attempt to 10 for easy, 5 for hard
    if difficulty == 'easy':
        return attempts_left + 10
    else:
        return attempts_left +5


# Start of script execution (Game intro)
print(f'Welcome to the number guessing game!')
print(f'Try to guess a number between 1 and 100!')
chosen_difficulty = input(f'Please choose a difficulty: type "easy" or "hard": ')
attempts_left = 0
attempts_left = set_difficulty(chosen_difficulty)
print(f'You have chosen {chosen_difficulty}, you will have {attempts_left} attempts!')
mystery_number = random.randint(1,100)
print(f"for dev, number is {mystery_number}")
# Start game 
# attmepts is now 10 or 5 
#ask player to choose number 
while attempts_left > 0:
    chosen_number = int(input(f'Please choose a number between 1 and 100'))
    #compare chosen number and mystery number 
    if chosen_number == mystery_number:
        print(f"You chose the correct number!! You WIN!! HOORAY!!")
    elif chosen_number > mystery_number:
        print(f"Too high")
        attempts_left -=1
        print(f"You have {attempts_left} attempts left")
    else: 
        print(f"Too Low")
        attempts_left -=1
        print(f"You have {attempts_left} attempts left")
        
print(f"You have used up all your attempts, try harder next time!")

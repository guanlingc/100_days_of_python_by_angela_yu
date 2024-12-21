import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

images=[rock,paper, scissors]
# start of script
print(f'Welcome to a rock paper scissor simulation!! Play against a RNG')
# input for user
user_input = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n'))
# input for pc
computer_input = random.randint(0,2)

print(images[user_input])
print(f'Computer chose:')
print(images[computer_input])

# decision making
# 'What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.

if user_input >= 3 or user_input < 0:
    print(f'You typed an invalid number. Please restart')

elif user_input == 0 and computer_input == 2:
    print(f'You win!!')

elif computer_input == 0 and user_input == 2:
    print(f'You lose!')
elif computer_input > user_input:
    print(f'You lose!')
elif user_input > computer_input:
    print(f'You win!')
elif user_input == computer_input:
    print(f'Draw')
else:
    print(f'You lose')


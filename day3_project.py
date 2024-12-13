print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice1 = input('You enter a cave and you see 2 paths, which path do you choose? Left or Right? \n').lower()

if choice1 == 'left':
    print(f'you find yourself arrived at a lake. In the middle of the lake, you see a treasure chest')
    choice2 = input(f'what do you do? Swim or Wait? \n')
else:
    print(f'You fell into a pit full of snakes and you died')

if choice2 == 'Swim':
    print(f'You turn around and the way back is gone, instead you see 3 doors')
    choice3 = input(f'Which door do you choose? Red, Yellow or Blue? \n')
else:
    print(f'You encounter some a giant carnivorus trout and you are eaten by it you died')

if choice3 == 'Red':
    print(f'You open the door and a dragon breathes fire at you, you burnt to death')

elif choice3 == 'Blue':
    print(f'You open the door and an alien shoots a beam at you, you burnt to death')

elif choice3 == 'Yellow':
    print(f'you win!')
else:
    print(f'game over')
# This script is meant for the solution for the "Maze" Challenge at
# https://reeborg.ca/reeborg.html

def turn_right():
    # makes robot face the right
    turn_left()
    turn_left()    
    turn_left()
    
def check_next_direction():
    # faces a direction without a wall
    while wall_in_front() == True:
        turn_left()

def follow_wall():
    while wall_on_right() == True and wall_in_front() == False:
        move()
        
def navigate_corner():
    turn_right()
    move()
    
        
while at_goal()!= True:
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
        
from turtle import Turtle, Screen
import turtle
import random
wugui = Turtle()

turtle.colormode(255)
wugui.shape('classic')
wugui.color('Darkolivegreen')

angle = [0,90,180,270]
colors = ['red','green','blue','orange','yellow','black','pink','purple']

def random_colors():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)

# total interior angle = 360
# Draw Shape
# for i in range(3,11):
#     interior_angle = (i-2) * 180 / i
#     exterior_angle = 180 - interior_angle
#     print(exterior_angle)
#     wugui.pencolor(random.choice(colors))
#     for _ in range(i):
#         wugui.forward(100)
#         wugui.right(exterior_angle)
    
# Random Walk
# for _ in range(300):
#     wugui.setheading(random.choice(angle))
#     wugui.pencolor(random_colors())
#     wugui.pensize(10)
#     wugui.forward(20)
#     wugui.speed(10)

# Spirograph
wugui.speed("fastest")
for i in range(360):
    wugui.pencolor(random_colors())
    wugui.circle(100)
    wugui.left(1)


screen = Screen()
screen.exitonclick()


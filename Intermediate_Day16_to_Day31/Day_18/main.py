from turtle import Turtle, Screen
import random
import turtle

color_list = [(203, 172, 108), (153, 180, 195), 
              (152, 186, 174), (193, 161, 176), (214, 203, 113), (208, 179, 195),
              (168,192,219) , (188,180,171),(162,214,202),(155,216,175)]
turtle.colormode(255)



def paint_dots():
    for i in range(0,9):
        wugui.color(random.choice(color_list))
        # wugui.pensize(20)
        wugui.stamp()
        wugui.forward(50)
        
# wugui.penup()
wugui = Turtle()
wugui.speed("fastest")
wugui.penup()
wugui.shape('circle')
y_coor = -200
wugui.teleport(-200,y_coor)
for i in range(10):
    paint_dots()    
    y_coor += 50
    wugui.teleport(-200,y_coor)

wugui.hideturtle()

screen = Screen()
screen.exitonclick()
# 10 by 10 dots
# width 20
# spacing 50

# import colorgram
# # Extract 6 colors from an image.
# colors = colorgram.extract('image.jpg', 10)
# # print(colors)
# all_colors = []
# for color in colors:
#     r=color.rgb.r
#     g=color.rgb.g
#     b=color.rgb.b
#     rgb = (r,g,b)
#     all_colors.append(rgb)

# print(all_colors)
# colorgram.extract returns Color objects, which let you access
# RGB, HSL, and what proportion of the image was that color.
# first_color = colors[0]
# rgb = first_color.rgb # e.g. (255, 151, 210)
# hsl = first_color.hsl # e.g. (230, 255, 203)
# proportion  = first_color.proportion # e.g. 0.34

# # RGB and HSL are named tuples, so values can be accessed as properties.
# # These all work just as well:
# red = rgb[0]
# red = rgb.r
# saturation = hsl[1]
# saturation = hsl.s

# import turtle 
# from turtle import Turtle, Screen

# wugui = turtle.Turtle()
# wugui2 = Turtle()
# print(wugui)
# print(wugui2)
# wugui.shape("turtle")
# wugui.color('DarkOrange','DarkGreen')
# wugui.forward(100)
# print(wugui.color())
# screen = Screen()
# print(screen.canvheight)
# screen.exitonclick()

from prettytable import PrettyTable
# create an object using a class
table = PrettyTable()
# call object functions
table.add_column("Pokemon", ["Pikachu","Squirtle","Charmander"])
table.add_column("Type", ["Electric","Water","Fire"])
# set object's attribute
table.align = "l"
print(table)
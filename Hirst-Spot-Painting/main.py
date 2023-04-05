import colorgram
from turtle import Turtle, Screen
import random

turtle = Turtle(visible=False)

screen = Screen()
screen.colormode(255)


turtle.penup()
turtle.goto(-screen.window_width()/2 + 20, -screen.window_height()/2 + 20) 
turtle.pendown()
turtle.speed("fastest")





colors = colorgram.extract('hirst.jpg', 20)

for _ in range(3):
    colors.pop(0)

rgb_colors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r,g,b)
    rgb_colors.append(new_color)
print(rgb_colors)


def up():
    turtle.penup()
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(1000)
    turtle.right(180)
    turtle.pendown()


for _ in range(16):
    for _ in range(20):
        turtle.dot(20, random.choice(rgb_colors))
        turtle.penup()
        turtle.forward(50)
        turtle.pendown()
    up()
screen.exitonclick()
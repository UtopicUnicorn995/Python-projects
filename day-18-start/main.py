import turtle
from turtle import Turtle, Screen
import random

def pick_color():
    colors = ["blue","black","brown","red","yellow","green","orange","beige","turquoise","pink"]
    random.shuffle(colors)
    return colors[0]

def walk_sides():
    sides = [90,  180, 270, 0]
    return random.choice(sides)


timmy = Turtle()
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colors = (r, g, b)
    return random_colors


timmy.speed('fastest')
timmy.pensize(1)


for i in range(360):
    timmy.circle(100)
    timmy.left(180)
    timmy.color(random_color())
    timmy.hideturtle()

screen = Screen()
screen.exitonclick()

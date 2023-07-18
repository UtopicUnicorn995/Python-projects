# import colorgram
#
# colors = colorgram.extract('image.jpg', 35)
#
# color_pallete = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb = (r, g, b)
#     color_pallete.append(rgb)
#
# print(color_pallete)
import turtle
from turtle import Turtle, Screen
import random
color_list = [(58, 106, 147), (235, 227, 209), (224, 201, 112), (132, 86, 60), (220, 140, 70), (195, 145, 170), (139, 176, 201), (238, 225, 234), (138, 80, 104), (189, 82, 112), (211, 93, 66), (67, 108, 92), (133, 181, 136), (130, 135, 77), (63, 156, 96), (47, 156, 190), (184, 192, 202), (216, 175, 188), (17, 58, 92), (23, 67, 111), (113, 123, 150), (126, 39, 49), (231, 175, 162), (156, 207, 216), (171, 205, 184), (68, 56, 42), (78, 64, 46), (46, 76, 69), (142, 39, 34), (19, 91, 105), (46, 67, 59)]
x = -200
y = -200
turtle.colormode(255)
arrow = Turtle()
arrow.penup()
arrow.setposition(x, y)
arrow.width(8)
arrow.hideturtle()

print(random.choice(color_list))
print(arrow.fillcolor())
for _ in range(10):
    for _ in range(10):
        arrow.pendown()
        arrow.dot(20, random.choice(color_list))
        arrow.penup()
        arrow.forward(40)
    y += 40
    arrow.setposition(x, y)


Screen().exitonclick()

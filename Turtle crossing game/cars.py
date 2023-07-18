from turtle import Turtle
import random
import time


class Car(Turtle):
    def __init__(self, color):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.color(color)
        self.x_cor = random.randrange(-400, 430)
        self.y_cor = random.randrange(-310, 310)
        self.goto(self.x_cor, self.y_cor)

    def car_move(self):
        self.x_cor -= 20
        self.goto(self.x_cor, self.y_cor)

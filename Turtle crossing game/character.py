from turtle import Turtle


class Character(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.left(90)
        self.penup()
        self.y_axis = -330
        self.goto(0, self.y_axis)
        self.move()

    def move(self):
        self.y_axis += 20
        self.goto(0, self.y_axis)

    def user_reset(self):
        self.y_axis = -330
        self.goto(0, self.y_axis)

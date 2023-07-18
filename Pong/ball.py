from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        ball_xcor = self.xcor() + self.x_move
        ball_ycor = self.ycor() + self.y_move
        self.goto(ball_xcor, ball_ycor)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_move(self):
        self.home()
        self.bounce_x()
        self.move_speed = 0.1

    # def increase_speed_l(self):
    #     self.x_move -= 1
    #     self.y_move -= 1
    #     print(self.x_move)

    # def increase_speed_r(self):
    #     self.x_move += 1
    #     self.y_move += 1
    #     print(self.x_move)

from turtle import Screen
from paddle import Paddle
from ball import Ball

from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

paddle_right = Paddle(350, 0)
paddle_left = Paddle(-350, 0)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle_right.go_up, "Up")
screen.onkey(paddle_right.go_down, "Down")
screen.onkey(paddle_left.go_up, "w")
screen.onkey(paddle_left.go_down, "s")


game_is_on = True
while game_is_on:
    # time.sleep also increases the speed, in this case it'll speed up when it hits the paddle
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with the paddle
    if (
        ball.distance(paddle_right) < 50
        and ball.xcor() > 320
        or ball.distance(paddle_left) < 50
        and ball.xcor() < -320
    ):
        ball.bounce_x()

    if ball.distance(paddle_right) > 50 and ball.xcor() > 380:
        ball.reset_move()
        scoreboard.l_point()

    if ball.distance(paddle_left) > 50 and ball.xcor() < -380:
        ball.reset_move()
        scoreboard.r_point()

screen.exitonclick()

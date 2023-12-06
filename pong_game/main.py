from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PONG")
screen.tracer(0)

right_paddle = Paddle(350, 0)
left_paddle = Paddle(-350, 0)
pong_ball = Ball()
scorekeeper = Scoreboard()

screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(pong_ball.move_speed)
    pong_ball.move()
    # Detect collision with ceiling and floor
    if abs(pong_ball.ycor()) >= 280:
        pong_ball.bounce_y()
    # Detect collision with paddle
    if ((pong_ball.distance(right_paddle) < 60 and pong_ball.xcor() > 330)
            or (pong_ball.distance(left_paddle) < 60 and pong_ball.xcor() < -330)):
        pong_ball.bounce_x()

    # Detect right side paddle miss
    if pong_ball.xcor() > 360:
        pong_ball.reset_position()
        scorekeeper.l_point()

    # Detect left side paddle miss
    if pong_ball.xcor() < -360:
        pong_ball.reset_position()
        scorekeeper.r_point()

screen.exitonclick()

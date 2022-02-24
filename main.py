from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreBoard import ScoreBoard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.bgcolor('black')
screen.listen()
screen.tracer(0)

r_paddle = Paddle(365)
l_paddle = Paddle(-375)

r_score = ScoreBoard(90)
l_score = ScoreBoard(-90)

ball = Ball()

screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_running = True
fast = 0.1
while game_is_running:
    screen.update()
    ball.move()
    time.sleep(fast)

    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.bounce_from_wall()
    #   Detect collisions with right paddle
    if ball.distance(r_paddle) < 32 and ball.xcor() > 305 or ball.distance(l_paddle) < 32 and ball.xcor() < -305:
        ball.bounce_from_paddle()
        fast /= 1.1

    # when R missed  the ball
    if ball.xcor() > 375:
        ball.start_in_center()
        l_score.add()
        fast = 0.1

    # L paddle missed the ball
    if ball.xcor() < -385:
        ball.start_in_center()
        r_score.add()
        fast = 0.1

screen.exitonclick()

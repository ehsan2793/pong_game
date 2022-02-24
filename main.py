from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.bgcolor('black')
screen.listen()
screen.tracer(0)

r_paddle = Paddle(375)
l_paddle = Paddle(-385)
ball = Ball()

screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_running = True

while game_is_running:
    screen.update()
    ball.move()
    time.sleep(0.2)

    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.bounce()

screen.exitonclick()

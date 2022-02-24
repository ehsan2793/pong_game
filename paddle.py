from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x, y=0):
        super().__init__()
        self.penup()
        self.shape('square')
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.setposition(x=x, y=y)
        self.up_down_speed = 20

    def go_up(self):
        new_ycor = self.ycor() + self.up_down_speed
        self.sety(new_ycor)

    def go_down(self):
        new_ycor = self.ycor() - self.up_down_speed
        self.sety(new_ycor)

    def add_to_speed(self):
        self.up_down_speed *= 1.05

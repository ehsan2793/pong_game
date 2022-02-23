from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x, y=0):
        super().__init__()
        self.shape('square')
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.setposition(x=x, y=y)

    def go_up(self):
        new_ycor = self.ycor() + 20
        self.sety(new_ycor)

    def go_down(self):
        new_ycor = self.ycor() - 20
        self.sety(new_ycor)

from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.shape('circle')

    def move(self):
        x = self.xcor() + 10
        y = self.ycor() + 10
        self.setposition(x=x, y=y)

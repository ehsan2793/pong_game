from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.shape('circle')
        self.x_move = 10
        self.y_move = 10

    def move(self):
        x = self.xcor() + self.x_move
        y = self.ycor() + self.y_move
        self.setposition(x=x, y=y)

    def bounce(self):
        self.y_move = - self.y_move
        y = self.ycor() + self.y_move
        self.sety(y)

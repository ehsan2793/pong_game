from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self, x, y=250):
        super().__init__()

        self.color('white')
        self.penup()
        self.hideturtle()
        self.score = 0
        self.position = (x, y)
        self.update_score()

    def update_score(self):
        self.setposition(self.position)
        self.clear()
        self.write(arg=f' {self.score}', move=True, font=('times', 40, "bold"))

    def add(self):
        self.score += 1
        self.update_score()

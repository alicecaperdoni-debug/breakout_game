from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(position)

        self.stretch_len = 10
        self.shapesize(stretch_wid=1, stretch_len=self.stretch_len)

    def shrink(self, amount=1, min_len=2):
        if self.stretch_len > min_len:
            self.stretch_len = max(min_len, self.stretch_len - amount)
            self.shapesize(stretch_wid=1, stretch_len=self.stretch_len)

    def go_right(self):
        new_x = self.xcor() + 20
        self.goto(new_x, self.ycor())

    def go_left(self):
        new_x = self.xcor() - 20
        self.goto(new_x, self.ycor())

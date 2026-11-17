from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.stretch_len = 10
        self.shapesize(stretch_wid=1, stretch_len=self.stretch_len)
        self.penup()
        self.goto(position)

    def go_right(self):
        new_x = self.xcor() + 20
        self.goto(new_x, self.ycor())

    def go_left(self):
        new_x = self.xcor() - 20
        self.goto(new_x, self.ycor())

    # def paddle_shrinks(self):
    #     self.stretch_len -= 5
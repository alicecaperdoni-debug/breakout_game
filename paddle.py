from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=10)  # la turtle parte sempre da 20x20, riguarda turtle.shapesize
        self.penup()
        self.goto(position)

    def go_right(self):
        new_x = self.xcor() + 20
        self.goto(self.xcor(), new_x)

    def go_left(self):
        new_x = self.xcor() - 20
        self.goto(self.xcor(), new_x)
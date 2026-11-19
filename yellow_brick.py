from turtle import Turtle

POSITIONS = [-362, -297, -232, -167, -102, -37, 28, 93, 158, 223, 288, 353]

class YellowBrick:
    def __init__(self):
        super().__init__()
        self.segments = []
        self.create_brick()

    def create_brick(self):
        for position in POSITIONS:
            self.add_brick((position, 60))
            self.add_brick((position, 85))

    def add_brick(self, position):
        new_brick = Turtle(shape="square")
        new_brick.shapesize(stretch_wid=1, stretch_len=3)
        new_brick.color("yellow")
        new_brick.penup()
        new_brick.goto(position)
        self.segments.append(new_brick)
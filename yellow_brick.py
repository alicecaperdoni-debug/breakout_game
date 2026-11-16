from turtle import Turtle

### DA PROGETTO SNAKE
# STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
#
# class Snake:
#     def __init__(self):
#         self.segments = []
#         self.create_snake() # così quando credo l'oggetto succede questo
#         self.head = self.segments[0] # visto che sarà usata spesso, per semplificare la lettura
#
#     def create_snake(self):
#         for position in STARTING_POSITIONS:
#             self.add_segment(position)
#
#     def add_segment(self, position):
#         new_segment = Turtle(shape="square")
#         new_segment.color("white")
#         new_segment.penup()
#         new_segment.goto(position)
#         self.segments.append(new_segment)


POSITIONS = [()]

class Brick(Turtle):
    def __init__(self, position, color):
        super().__init__()
        self.shape("square")
        self.color(color)
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.goto(position)

    def add_brick(self):
        pass

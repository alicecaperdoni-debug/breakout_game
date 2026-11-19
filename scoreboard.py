from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.turns = 3
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self  ):
        self.clear()
        self.goto(-100, 260)
        self.write(f"Turni: {self.turns}", align="center", font=("Courier", 20, "normal"))
        self.goto(100, 260)
        self.write(f"Punti: {self.score}", align="center", font=("Courier", 20, "normal"))

    def lost_turn(self):
        self.turns -= 1
        self.update_scoreboard()

    def point(self, points):
        self.score += points
        self.update_scoreboard()
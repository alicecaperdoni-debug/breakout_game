from turtle import Screen
from paddle import Paddle
from yellow_brick import YellowBrick
from red_brick import RedBrick
from orange_brick import OrangeBrick
from green_brick import GreenBrick
import time

s = Screen()
s.bgcolor("black")
s.setup(width=800, height=600)
s.title("Alice's Breakout")
s.tracer(0)

#TODO ball object + speed increase

r_brick = RedBrick()
o_brick = OrangeBrick()
g_brick = GreenBrick()
y_brick = YellowBrick()

p = Paddle((0, -200))

s.listen()
s.onkeypress(p.go_right, "d")
s.onkeypress(p.go_left, "a")
s.update()

#TODO while game on, scoring [+ scoreboard object) and lives
# -bricks spariscono

#TODO i bricks si ricreano dopo che sono spariti tutti [gioco originale solo due schermate]

s.exitonclick()
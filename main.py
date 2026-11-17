from turtle import Screen
from paddle import Paddle
from yellow_brick import YellowBrick
from red_brick import RedBrick
from orange_brick import OrangeBrick
from green_brick import GreenBrick
from ball import Ball
import time

s = Screen()
s.bgcolor("black")
s.setup(width=800, height=600)
s.title("Alice's Breakout")
s.tracer(0)

r_brick = RedBrick()
o_brick = OrangeBrick()
g_brick = GreenBrick()
y_brick = YellowBrick()

ball = Ball()
paddle = Paddle((0, -200))

s.listen()
s.onkeypress(paddle.go_right, "d")
s.onkeypress(paddle.go_left, "a")

#TODO ball object + speed increase
#TODO while game on, scoring [+ scoreboard object) and lives
# -bricks spariscono

game_on = True

while game_on:
    time.sleep(ball.move_speed)
    s.update()
    ball.move()

    #TODO capisci come far rimpicciolire il paddle

    # detect collision with upper wall
    if ball.ycor() > 280:
        ball.bounce_up_y()
        # paddle.stretch_len = paddle.stretch_len - 1

    # detect collision with right and left walls
    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.bounce_x()

    # detect collision with paddle
    if ball.distance(paddle) < 50 and ball.ycor() < -170:
        ball.bounce_up_y()
    #
    # # detect when paddle misses
    # if ball.xcor() > 380:
    #     ball.reset_position()
    #     scoreboard.l_point()



#TODO i bricks si ricreano dopo che sono spariti tutti [gioco originale solo due schermate]

s.exitonclick()
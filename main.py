from turtle import Screen
from paddle import Paddle
from yellow_brick import YellowBrick
from red_brick import RedBrick
from orange_brick import OrangeBrick
from green_brick import GreenBrick
from ball import Ball
from scoreboard import Scoreboard
import time

s = Screen()
s.bgcolor("black")
s.setup(width=800, height=600)
s.title("Alice's Breakout")
s.tracer(0)

scoreboard = Scoreboard()

r_brick = RedBrick()
o_brick = OrangeBrick()
g_brick = GreenBrick()
y_brick = YellowBrick()

ball = Ball()
paddle = Paddle((0, -200))

s.listen()
s.onkeypress(paddle.go_right, "d")
s.onkeypress(paddle.go_left, "a")

game_on = True

while game_on:
    time.sleep(ball.move_speed)
    s.update()
    ball.move()

    # TODO continua solo ci sono ancora turni disponibili

    #TODO capisci come far rimpicciolire il paddle; vuoi far fermare il paddle contro il muro?

    # detect collision with upper wall
    if ball.ycor() > 280:
        ball.bounce_up_y()
        # paddle.stretch_len = paddle.stretch_len - 1

    # detect collision with right and left walls
    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.bounce_x()

    # detect collision with paddle
    if ball.distance(paddle) < 100 and ball.ycor() < -170:
        ball.bounce_up_y()

    # detect when paddle misses
    if ball.ycor() < -230:
        ball.reset_position((paddle.xcor(), paddle.ycor()+30))
        scoreboard.lost_turn()

    # detect collision with bricks
    for brick in y_brick.segments:
        if ball.distance(brick) < 50 and ((ball.ycor() < brick.ycor() - 25) or (ball.ycor() < brick.ycor() + 25)):
            ball.bounce_up_y()
            brick.hideturtle()
            y_brick.segments.remove(brick)
            scoreboard.point(1)

    for brick in g_brick.segments:
        if ball.distance(brick) < 50 and ((ball.ycor() < brick.ycor() - 25) or (ball.ycor() < brick.ycor() + 25)):
            ball.bounce_up_y()
            brick.hideturtle()
            g_brick.segments.remove(brick)
            scoreboard.point(3)

    for brick in o_brick.segments:
        if ball.distance(brick) < 50 and ((ball.ycor() < brick.ycor() - 25) or (ball.ycor() < brick.ycor() + 25)):
            ball.bounce_up_y()
            brick.hideturtle()
            o_brick.segments.remove(brick)
            scoreboard.point(5)

    for brick in r_brick.segments:
        if ball.distance(brick) < 50 and ((ball.ycor() < brick.ycor() - 25) or (ball.ycor() < brick.ycor() + 25)):
            ball.bounce_up_y()
            brick.hideturtle()
            r_brick.segments.remove(brick)
            scoreboard.point(7)

#TODO ball object speed increase

#TODO i bricks si ricreano dopo che sono spariti tutti [gioco originale solo due schermate]

s.exitonclick()
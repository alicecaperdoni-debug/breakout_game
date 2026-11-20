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
final_game = False
hits = 0

while game_on:
    if hits == 4 or hits == 12:
        ball.move_speed *= 0.999
    time.sleep(ball.move_speed)
    s.update()
    ball.move()

    # detect collision with upper wall
    if ball.ycor() > 280:
        ball.bounce_up_y()
        paddle.shrink()

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
        if scoreboard.turns <= 0:
            game_on = False

    # detect collision with bricks
    for brick in y_brick.segments:
        if ball.distance(brick) < 50 and ((ball.ycor() < brick.ycor() - 25) or (ball.ycor() < brick.ycor() + 25)):
            ball.bounce_up_y()
            brick.hideturtle()
            y_brick.segments.remove(brick)
            hits += 1
            scoreboard.point(1)

    for brick in g_brick.segments:
        if ball.distance(brick) < 50 and ((ball.ycor() < brick.ycor() - 25) or (ball.ycor() < brick.ycor() + 25)):
            ball.bounce_up_y()
            brick.hideturtle()
            g_brick.segments.remove(brick)
            hits += 1
            scoreboard.point(3)

    for brick in o_brick.segments:
        if ball.distance(brick) < 50 and ((ball.ycor() < brick.ycor() - 25) or (ball.ycor() < brick.ycor() + 25)):
            ball.bounce_up_y()
            brick.hideturtle()
            o_brick.segments.remove(brick)
            hits += 1
            scoreboard.point(5)
            ball.move_speed *= 0.999

    for brick in r_brick.segments:
        if ball.distance(brick) < 50 and ((ball.ycor() < brick.ycor() - 25) or (ball.ycor() < brick.ycor() + 25)):
            ball.bounce_up_y()
            brick.hideturtle()
            r_brick.segments.remove(brick)
            hits += 1
            scoreboard.point(7)
            ball.move_speed *= 0.999

    # Build again or winning
    if len(y_brick.segments) == 0 and len(g_brick.segments) == 0 and len(o_brick.segments) == 0 and len(r_brick.segments) == 0:
        if final_game:
            scoreboard.winner()
        else:
            final_game = True
            y_brick.create_brick()
            g_brick.create_brick()
            o_brick.create_brick()
            r_brick.create_brick()

    if len(y_brick.segments) == 0:
        if final_game:
            game_on = False
            scoreboard.winner()
        else:
            final_game = True
            y_brick.create_brick()

if not game_on and scoreboard.turns <= 0:
    scoreboard.game_over()


s.exitonclick()
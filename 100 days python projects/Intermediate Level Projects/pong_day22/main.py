import turtle, paddle
from paddle import Paddle
from ball import Ball
from turtle import *
import time
from scoreboard import Score
a = Screen()

a.bgcolor("black")
a.title("Arsh's Pong Game")
a.setup(width=800, height=600)
score = Score()
a.tracer(0)
b1 = Paddle((350, 0))
b2 = Paddle( (-350, 0))

ball = Ball()

a.listen()
a.onkey(key="i", fun=b1.go_up)
a.onkey(key="k", fun=b1.go_down)
a.onkey(key="w", fun=b2.go_up)
a.onkey(key="s", fun=b2.go_down)

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    a.update()
    ball.move()
    if ball.ycor() > 280.00 or ball.ycor()<-280:
        ball.bounce_y()
    if ball.distance(b1)< 50 and ball.xcor() > 320 or ball.distance(b2)<50 and ball.xcor()<-320:

        ball.bounce_x()
    if ball.distance(b1)>50 and ball.xcor()>380:
        score.l_point()
        ball.reset_ball()
        ball.bounce_x()
    if ball.distance(b2) > 50 and ball.xcor() < -380:
        score.r_point()
        ball.reset_ball()

        ball.bounce_x()



a.exitonclick()

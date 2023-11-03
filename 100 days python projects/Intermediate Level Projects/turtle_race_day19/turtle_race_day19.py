import turtle
from turtle import Turtle, Screen
import random

a = Screen()
a.setup(width=500,height=400)
turtle.colormode(255)
blue = Turtle(shape="turtle")
blue.color("blue")
green = Turtle(shape="turtle")
green.color("green")
violet = Turtle(shape="turtle")
violet.color("violet")
brown = Turtle(shape="turtle")
brown.color('brown')
yellow = Turtle(shape="turtle")
yellow.color('yellow')
black = Turtle(shape="turtle")


blue.penup()
blue.goto(-250, 0)
green.penup()
green.goto(-250, 180)
violet.penup()
violet.goto(-250, -180)
brown.penup()
brown.goto(-250, 90)
yellow.penup()
yellow.goto(-250, -90)
black.penup()
black.goto(230, 200)
black.pendown()
black.goto(230, -200)
black.left(90)
l = [blue, yellow, violet, brown, green]
res = a.textinput(title="Make your bet: ", prompt="Which turtle would win the race?")
is_race_on = False
if res:
    is_race_on = True
while is_race_on:
    for turtle in l:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_turtle = turtle.pencolor()
            if res == winning_turtle:
                print(f"You won! The winner is {winning_turtle}")
            else:
                print(f"You lost! The winner is {winning_turtle}")
        else:
            turtle.speed(5)
            turtle.forward(random.randint(1,10))

a.exitonclick()
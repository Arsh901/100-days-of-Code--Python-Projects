
import turtle
import random
turtle.colormode(255)
from turtle import *
tim = Turtle()
tim.shape("circle")
tim.shapesize(1)
colours = [(201, 164, 112), (238, 246, 241), (152, 75, 49), (221, 201, 138), (171, 153, 42), (56, 95, 126),
              (139, 31, 19), (134, 163, 184), (197, 93, 73), (48, 121, 88), (98, 75, 77), (142, 178, 148), (75, 41, 33),
              (165, 145, 156), (15, 99, 71), (234, 175, 164), (54, 45, 47), "red", "brown", "pink"]
tim.color("white")
tim.penup()
tim.right(135)
tim.forward(300)
tim.left(135)
def move():
    tim.color("red")
    tim.left(90)
    tim.penup()
    tim.color("white")
    tim.forward(50)
    tim.left(90)
    tim.forward(500)
    tim.left(180)
    tim.pendown()
tim.speed(20)

for i in range(11):
    for i in range(10):
        tim.color(random.choice(colours))
        tim.dot(30, random.choice(colours))
        tim.penup()
        tim.forward(50)
        tim.pendown()
    move()

a = Screen()
a.exitonclick()
from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("red")
        self.shapesize(0.8)
        self.penup()
        self.appear()

    def appear(self):
        self.goto(random.randint(-250,250),random.randint(-250,250))











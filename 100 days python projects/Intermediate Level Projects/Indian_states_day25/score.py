import turtle
from turtle import *

class Score_board(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(230,260)

    sc = 0

    def write_sc(self):
        self.clear()
        self.write(f"Score : {self.sc}", align="center", font=("Ariel", 20, "normal"))

    def increment(self):
        self.sc += 1

    def completion(self):
        self.goto(0,0)
        self.write("You Won!!", align="center", font=("Ariel", 40, "normal"))






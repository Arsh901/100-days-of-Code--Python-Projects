import random

import pandas, turtle, score
from pandas import *
from turtle import *
import time
a = Screen()
a.setup(700,700)
a.title("Indian State Game")
new_image = "project_image.gif"
a.addshape(new_image)
turtle.shape(new_image)

tim = Turtle()
tim.hideturtle()
tim.penup()

james = Turtle()
james.hideturtle()
james.penup()
james.color("blue")
james.write("Welcome to Indian state guessing game!!", align="center", font=("Ariel", 20, "normal"))
time.sleep(1.8)
james.clear()
james.write("Made by Arsh as a project", align="center", font=("Ariel", 20, "normal"))
time.sleep(1.8)
james.clear()
james.write("You need to guess atleast 29 states to win",align="center", font=("Ariel", 20, "normal"))
time.sleep(1.8)
james.clear()

scor = score.Score_board()
color_list = ["blue", "brown", "black", "red" ]
database = pandas.read_csv("new_file.csv")
state_list = database.state.to_list()
scor.write_sc()

already_gave = []

while scor.sc <29:
    answer_value = a.textinput(title="Guess the state!!", prompt="Enter a name:").title()
    if answer_value == "Exit":
        break

    if answer_value in already_gave:
        james.write("You already guessed this one!", align="center", font=("Ariel", 20, "normal"))
        time.sleep(1.5)
        james.clear()

    elif answer_value in state_list:
        already_gave.append(answer_value)
        scor.increment()
        scor.write_sc()
        var = database[database.state == answer_value]
        tim.goto(x=int(var.x.iloc[0]), y=int(var.y.iloc[0]))
        tim.color(random.choice(color_list))
        tim.write(answer_value, align="center", font=("Ariel", 10, "normal"))

    if scor.sc == 29:
        scor.completion()


a.exitonclick()





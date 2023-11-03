from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        with open("current_score.txt", mode="r") as cr:
            self.high_score = int(cr.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(-280,260)
        self.print_score()

    def increase_score(self):
        self.level +=1
        self.print_score()

    def print_score(self):
        self.clear()
        self.goto(-280, 260)
        self.write(f"                                                                                               Score: {self.level} High score: {self.high_score}", align="center", font=("Arial", 16, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over", align="center", font=("Arial", 16, "normal"))

    def reset_game(self):
        if self.level>self.high_score:
            self.high_score=self.level
            with open("current_score.txt",mode="w") as cr:
                cr.write(f"{self.high_score}")
        self.level = 0
        self.print_score()




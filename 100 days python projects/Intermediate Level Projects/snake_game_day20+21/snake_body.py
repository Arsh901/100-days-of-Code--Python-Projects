from turtle import *
l = [0,-20,-40]
class Snake(Turtle):
    def __init__(self):
        self.list_of_blocks = []
        self.make_snake()

    def make_snake(self):

        for i in l:
            new_block = Turtle("circle")
            new_block.color("yellow")
            new_block.penup()
            new_block.goto(x=i, y=0)
            self.list_of_blocks.append(new_block)

    def movement(self):

        for i in range(len(self.list_of_blocks)-1, 0, -1):
            new_x = self.list_of_blocks[i - 1].xcor()
            new_y = self.list_of_blocks[i - 1].ycor()
            self.list_of_blocks[i].goto(new_x, new_y)
        self.list_of_blocks[0].forward(20)

    def left_move(self):
        if self.list_of_blocks[0].heading() !=0:

            self.list_of_blocks[0].setheading(180)
    def right_move(self):
        if self.list_of_blocks[0].heading() !=180:
            self.list_of_blocks[0].setheading(0)
    def up_move(self):
        if self.list_of_blocks[0].heading() !=270:
            self.list_of_blocks[0].setheading(90)

    def down_move(self):
        if self.list_of_blocks[0].heading() !=90:
            self.list_of_blocks[0].setheading(270)

    def size_increase(self):
        new_block = Turtle("circle")
        new_block.color("yellow")
        new_block.penup()
        new_block.goto(self.list_of_blocks[-1].xcor()-20,self.list_of_blocks[-1].ycor()-20)
        self.list_of_blocks.append(new_block)

    def stop_snake(self):
        self.list_of_blocks.clear()







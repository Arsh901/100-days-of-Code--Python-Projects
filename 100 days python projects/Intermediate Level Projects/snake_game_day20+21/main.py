from turtle import *
import time
from snake_body import Snake
from food import Food
from scoreboard import Score


a = Screen()
a.setup(600,600)
a.bgcolor("black")
a.title("Arsh's Snake Game")
a.tracer(0)
snakes = Snake()
food = Food()
score = Score()
a.listen()
a.onkey(key="a",fun=snakes.left_move)
a.onkey(key="d",fun=snakes.right_move)
a.onkey(key="w",fun=snakes.up_move)
a.onkey(key="s",fun=snakes.down_move)

game_is_on = True
while game_is_on:
    a.update()
    snakes.movement()
    if food.distance(snakes.list_of_blocks[0])<20:
        score.increase_score()
        
        snakes.size_increase()
        food.appear()

    if snakes.list_of_blocks[0].xcor()>300 or snakes.list_of_blocks[0].xcor()<-300 or snakes.list_of_blocks[0].ycor()>300 or snakes.list_of_blocks[0].ycor()<-300:
        # score.game_over()
        # game_is_on = False
        score.reset_game()
        score.game_over()
        game_is_on = False

    for i in snakes.list_of_blocks:
        if i == snakes.list_of_blocks[0]:
            pass
        elif snakes.list_of_blocks[0].distance(i) < 10:
            # game_is_on = False
            # score.game_over()
            score.reset_game()
            score.game_over()
            game_is_on = False

a.exitonclick()
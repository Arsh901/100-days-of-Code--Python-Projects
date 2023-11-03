import time
from turtle import *
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Arsh's Turtle Crossing Game")

screen.tracer(0)
player = Player()
car_manager = CarManager()
level = Scoreboard()
screen.listen()
screen.onkey(key="w", fun=player.move_up)


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
    if player.ycor()> 300:
        level.new_score()
        player.reset_turtle()
        car_manager.level_up()
        level.print_level()
    else:
        for i in car_manager.all_cars:
            if i.distance(player)<20:
                level.game_over()
                game_is_on  = False

screen.exitonclick()
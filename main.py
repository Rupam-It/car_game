# this is a game where to cross a road , road is full of car
import time 
from turtle import Turtle,Screen
from player import Player
from car_manager import Carmanager
from scoreboard import Scoreboard



screen= Screen()
screen.setup(600,600)
# screen.bgcolor("black")
screen.tracer(0)


player= Player()
car_manager=Carmanager()
scoreboard=Scoreboard()


screen.listen()
screen.onkey(player.move_up,"Up")


game_is_on=True
while game_is_on:
    time.sleep(.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_car()
    
    #detect collision with the car
    for car in car_manager.all_cars:
        if car.distance(player)<20:
            scoreboard.game_over()
            game_is_on=False
            
    # detect of successfull finishing
    if player.is_at_finish_line():
        player.goto_start()
        car_manager.level_up()
        scoreboard.score_update()

screen.exitonclick()
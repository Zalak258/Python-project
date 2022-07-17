import time
from turtle import Screen
from player import Player
from car_manager import CarManager
import random
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
screen.listen()
screen.onkeypress(player.move_up, "Up")
car_manager = []

game_is_on = True
movement = 0
moving_dist = 5
while game_is_on:

    if movement % 9 == 0:
        for i in range(random.randint(1, 4)):
            new_car = CarManager()
            car_manager.append(new_car)

    time.sleep(0.1)
    screen.update()
    for car in car_manager:
        car.move_car(moving_dist)
        if player.distance(car) < 20:
            game_is_on = False
        if player.distance(car) < 30 and car.xcor() <= 10:
            game_is_on = False

    if player.ycor() > 280:
        player.starting_pos()
        moving_dist += 3
        scoreboard.update()
    movement += 1

scoreboard.game_over()
screen.exitonclick()

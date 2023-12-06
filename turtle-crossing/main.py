import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from random import randint

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
scoreboard = Scoreboard()

# Initialize infinite number of cars
car_list = []
for i in range(100):
    car = CarManager(randint(-280, 6000), randint(-250, 250))
    car_list.append(car)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    screen.onkey(player.move, "Up")

    # Move cars
    for car in car_list:
        car.drive()

    # Detect when player successfully cross
    if player.detect_finish_line():
        player.reset_position()
        scoreboard.increase_score()
        scoreboard.update_scoreboard()
        for car in car_list:
            car.increase_speed()

    # Detect when play collide with a car
    for car in car_list:
        if player.distance(car) < 20:
            print("Collided! GG")
            game_is_on = False

screen.exitonclick()

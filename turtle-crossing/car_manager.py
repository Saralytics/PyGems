from turtle import Turtle
from random import randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 0


class CarManager(Turtle):
    def __init__(self, init_x, init_y):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=2)
        self.color(COLORS[randint(0, len(COLORS)-1)])
        self.penup()
        self.goto(init_x, init_y)
        self.speed = STARTING_MOVE_DISTANCE + MOVE_INCREMENT

    def drive(self):
        self.goto(self.xcor()-self.speed, self.ycor())

    def increase_speed(self):
        self.speed += 2


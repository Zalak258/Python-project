from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(1, 2)
        self.color(random.choice(COLORS))
        self.starting_pos()

    def starting_pos(self):
        self.goto(260, 22 * random.randint(-10, 10))
        self.setheading(180)

    def move_car(self, moving_dist):
        self.forward(moving_dist)

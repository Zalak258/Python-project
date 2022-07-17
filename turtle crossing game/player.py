from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
# FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.starting_pos()

    def starting_pos(self):
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move_up(self):
        self.forward(MOVE_DISTANCE)

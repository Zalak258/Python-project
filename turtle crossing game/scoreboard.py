from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('green')
        self.goto(-280, 260)
        self.level = 1
        self.write(f"Level : {self.level}", True, "left", ("Courier", 24, "normal"))
        self.hideturtle()

    def update(self):
        self.clear()
        self.level += 1
        self.goto(-280, 260)
        self.write(f"Level : {self.level}", True, "left", ("Courier", 24, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        self.write(f"Game Over", True, "center", ("arial", 30, "bold"))

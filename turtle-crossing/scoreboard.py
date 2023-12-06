from turtle import Turtle

FONT = ("Courier", 20, "normal")
ALIGNMENT = "center"
POSITION = (-240, 250)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(POSITION)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1

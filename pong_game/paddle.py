from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, initial_x, initial_y):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.goto(initial_x, initial_y)

    def go_up(self):
        """ The x cooordinate will never move """
        self.goto(self.xcor(), self.ycor() + 20)

    def go_down(self):
        """ The x cooordinate will never move """
        self.goto(self.xcor(), self.ycor() - 20)



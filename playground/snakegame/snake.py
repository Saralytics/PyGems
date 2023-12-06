import turtle

INITIAL_X = [0, -20, -40]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        """initialize the 3 dots, which makes up the starting snake body"""
        self.dots = []
        self.create_snake()
        self.head = self.dots[0]

    def create_snake(self):
        for i in INITIAL_X:
            new_dot = turtle.Turtle(shape="square")
            new_dot.color("white")
            new_dot.penup()
            new_dot.setx(i)
            self.dots.append(new_dot)

    def extend(self):
        new_dot = turtle.Turtle(shape="square")
        new_dot.color("white")
        new_dot.penup()
        new_dot.goto(self.dots[-1].position())
        self.dots.append(new_dot)

    def move(self):
        """IMPORTANT: How to move the snake body:
        # In the first iteration, we simply move each bock forward like this:
        # for dot in dots: dot.forward(20)
        # This creates a problem: if the first block changes direction, the rest of the body don't know how to follow.
        # Solution: ask the last dot(n) to go to the position of the second last dot(n-1),
        # and the n-1 dot go to the position of n-2 dot, and so on"""
        for i in range(len(self.dots) - 1, 0, -1):
            new_x = self.dots[i - 1].xcor()
            new_y = self.dots[i - 1].ycor()
            self.dots[i].goto(new_x, new_y)

        # after moving the rest of the body, we need to move the head, so the body can follow
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)



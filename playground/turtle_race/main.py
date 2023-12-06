import turtle
from random import randint

screen = turtle.Screen()
screen.setup(500, 400)
user_bet = screen.textinput("Make bet", "Pick the color of the winner: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtle_names = ["tim", "tam", "jon", "arya", "version", "tyrion"]
starting_coordinates = [(-200, -100), (-200, -60), (-200, -20), (-200, 20), (-200, 60), (-200, 100)]
all_turtles = []

for i, j, m in zip(turtle_names, colors, starting_coordinates):
    i = turtle.Turtle(shape="turtle")
    i.color(j)
    i.penup()
    i.goto(m[0], m[1])
    all_turtles.append(i)

if user_bet:
    is_game_on = True

# Move each turtle by a random distance
while is_game_on:
    for t in all_turtles:
        if t.xcor() > 230:
            print(t.pencolor())
            is_game_on = False
        t.forward(randint(0, 10))

screen.exitonclick()

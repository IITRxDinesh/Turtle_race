# import turtle
# from turtle import *
#
#
# tim = Turtle()
# screen = Screen()
#
#
# def forward():
#     new_turtle.forward(50)
#
#
# def backword():
#     new_turtle.forward(-50)
#
#
# def left():
#     new_turtle.left(10)
# def clear():
#     new_turtle.clear()
#     new_turtle.penup()
#     new_turtle.home()
#     new_turtle.pendown()
#
#
#
# def right():
#     new_turtle.right(10)
#
#
# screen.listen()
# screen.onkey(forward, "w")
# screen.onkey(backward , "s")
# screen.onkey(left, "a " )
# screen.onkey(right,"d")
# screen.onkey(clear,"c")
# turtle.done()
from turtle import Turtle, Screen

import turtle
from turtle import *
import random

screen = Screen()
is_race_on = False
all_turtles = []
colors = ["red", "orange", "yellow", "blue", "indigo", "violet"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []
screen.setup(width=500, height=400)
user_text = screen.textinput(title="Make your bet", prompt="Which turtle will win the match? Enter a color: ")
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(-250, y_positions[turtle_index])
    all_turtles.append(new_turtle)


if user_text:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            is_race_on=False
            if winning_color==user_text:
                print(f"You Won! The {winning_color} turtle is the winner.")
            else:
                print(f"You lost. The {winning_color} turtle is the winner.")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)





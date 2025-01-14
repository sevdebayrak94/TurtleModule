import turtle
from turtle import Turtle, Screen
import random


#### Screen #####
screen = Screen()
screen.setup(500,400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
#######
is_race_on = False
color = ["red", "blue", "green", "orange","yellow", "black"]
y_position = [-70,-40,-10,20,50,80]
all_turtles = []
for i in range(0,6):
    tim = Turtle(shape="turtle")
    tim.color(color[i])
    tim.penup()
    tim.goto(-230, y_position[i])
    all_turtles.append(tim)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won!, The {winning_color} turtle is the winner!")
            else:
                print(f"You've Lost!, The {winning_color} turtle is the winner!")

        random_distance = random.randint(0,10)
        turtle.forward(random_distance)


screen.exitonclick()
print(user_bet)
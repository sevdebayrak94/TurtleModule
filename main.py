import random
from random import randint
from turtle import *
tim = Turtle()

n=[3,4,5,6,7,8,9,10]
colors= ["blue", "yellow", "pink", "red", "orange", "green", "black", "DeepSkyBlue", "DarkOrchid" ]
for i in n:
    angle = 360 / i
    tim.color(random.choice(colors))
    for j in range(1, i+1):
        tim.right(angle)
        tim.forward(100)
        tim.heading()

screen = Screen()
screen.exitonclick()

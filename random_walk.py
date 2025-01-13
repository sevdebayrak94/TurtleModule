import turtle as t
import random
from turtle import Screen

tim = t.Turtle()

### Random Color
t.colormode(255)
def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r,g,b)

colors= ["blue", "yellow", "pink", "red", "orange", "green", "black", "DeepSkyBlue", "DarkOrchid" ]
directions = [0,90,180,270]
tim.pensize(15)
tim.speed("fast")
#Random Walk
for _ in range(100):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))


tim = Screen()
tim.exitonclick()
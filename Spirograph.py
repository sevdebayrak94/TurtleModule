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


tim.speed("fastest")
for i in range(360):
    tim.color(random_color())
    tim.circle(90)
    tim.left(5)

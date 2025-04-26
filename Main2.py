import turtle

from turtle import Turtle, Screen
import random

turtle.colormode(255)

tim = Turtle()
tim.shape("turtle")

def random_color():
    tim.pensize(10)
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

for i in range(3, 11):
    tim.pencolor(random_color())
    for j in range(i):
        tim.left(-360/i)
        tim.forward(100)

screen = Screen()
screen.exitonclick()


import turtle

from turtle import Turtle, Screen
import random
tim = Turtle()
tim.shape("turtle")
direction = [0, 90, 180, 270]

turtle.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

while(True):
    tim.pencolor(random_color())
    tim.pensize(10)
    tim.forward(20)
    tim.setheading(random.choice(direction))
screen = Screen()
screen.exitonclick()


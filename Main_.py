import turtle
from turtle import Turtle, Screen
import random
import colorgram
from matplotlib.pyplot import xcorr

#rgb_colors = []
#colors = colorgram.extract('image.jpg', 30)
#for color in colors:
#    r = color.rgb.r
#    g = color.rgb.g
#    b = color.rgb.b
#    rgb_colors.append((r, g, b))

#print(rgb_colors[2:])

turtle.colormode(255)
colors_list = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
tim = Turtle()

tim.hideturtle()
tim.setheading(225)
tim.penup()

tim.forward(300)
tim.setheading(-0)


for i in range (10):
    for _ in range (10):
        tim.pencolor(random.choice(colors_list))
        tim.dot(20)
        tim.forward(50)
    tim.setx(tim.xcor()-500)
    tim.sety(tim.ycor()+50)

screens = Screen()
screens.exitonclick()
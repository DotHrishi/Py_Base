import turtle as turtle_module
import random

turtle_module.colormode(255)
tim=turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()

color_list=[(155, 53, 78), (232, 119, 42), (39, 42, 62), (224, 122, 171), (13, 113, 193), (28, 171, 81), (60, 146, 4), (179, 51, 44), (19, 47, 44), (33, 27, 23), (236, 201, 1), (227, 193, 6), (225, 207, 90), (138, 164, 188), (126, 183, 135), (40, 33, 36), (223, 172, 193), (169, 100, 116), (164, 212, 168), (55, 56, 79), (181, 104, 86), (229, 176, 164), (88, 131, 172), (176, 191, 212), (72, 71, 46), (50, 70, 65)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots=100

for dot_count in range(1,number_of_dots+1):
    tim.dot(20,random.choice(color_list))
    tim.forward(50)

    if dot_count%10==0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen=turtle_module.Screen()
screen.exitonclick()
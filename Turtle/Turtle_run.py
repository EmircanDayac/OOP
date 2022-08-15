import random
from turtle import Turtle,Screen
screen = Screen()
screen.setup(500,500)


speed = [10,25,30]
yposition = [-70,-40,-10]
colors = ["red","green","purple"]




winner_prediction  = screen.textinput("How to winner turtle","")

turtle_array = []
for i in range(3):
    isbool = False
    tim= Turtle()
    tim.shape("turtle")
    tim.color(colors[i])
    tim.penup()
    tim.goto(-250,yposition[i])
    turtle_array.append(tim)
    if len(turtle_array) == 3:
        isbool = True

    while isbool:
       for turt in turtle_array:
           turt.forward(random.choice(speed))
           if turt.xcor() > 250:



               isbool = False







screen.exitonclick()
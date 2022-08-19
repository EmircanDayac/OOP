import random
import time
from turtle import Turtle

speed = [20, 30, 40, 50]
Cars_Generate_Position = [100, 200, -100, -200]
Cars = []

levelbool = False

class CarManager():
    def __init__(self):
        super().__init__()

        for j in range(3):
            Car = Turtle()
            Car.penup()
            Car.shape("square")
            Car.goto(Cars_Generate_Position[j], -200)
            Car.left(90)
            Cars.append(Car)
            print(len(Cars))
            if len(Cars) == 3:
                levelbool = True

        while levelbool:
            for turt in Cars:
                turt.forward(random.choice(speed))
                if turt.ycor() > 300:
                    turt.goto(random.choice(Cars_Generate_Position), -200)

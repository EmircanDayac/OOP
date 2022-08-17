import random
from turtle import Turtle



position = [200, -200]
d1 = random.choice(position)
d2 = random.choice(position)


class food(Turtle):
    a1 = d1
    a2 = d2
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(0.5)
        self.color("blue")
        self.penup()
        self.speed("fastest")
        self.goto(d1,d2)


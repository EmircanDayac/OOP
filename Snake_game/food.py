import random
from turtle import Turtle
import Game
game = Game()
position = [200,-200]
class food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(0.5)
        self.color("blue")
        self.penup()
        self.speed("fastest")
        a = self.goto(random.choice(position),random.choice(position))
        print(game.snakes_component[0].xcor())
        if(random.choice(position) == game.snakes_component[0].xcor()):
           print("trigger")


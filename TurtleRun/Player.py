from turtle import Turtle, Screen
from ScoreBoard import ScoreBoard
Y = ScoreBoard()
screen = Screen()
screen.listen()
turtle_list = []




class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("red")
        self.shape("turtle")
        self.goto(-250, 0)

        turtle_list.append(self)


def up():
    turtle_list[0].forward(20)
    if (turtle_list[0].xcor() > 290.0):
        Y.increase_Score()
        turtle_list[0].goto(-250, 0)


screen.onkey(up, "Up")

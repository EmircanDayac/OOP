from turtle import Turtle, Screen
from ScoreBoard import ScoreBoard

screen = Screen()
screen.listen()
turtle_list = []

ScoreBoard()


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
        ScoreBoard().increase_Score()
        print("giriyor")
        turtle_list[0].goto(-250, 0)


def GameOver():
    pass


screen.onkey(up, "Up")

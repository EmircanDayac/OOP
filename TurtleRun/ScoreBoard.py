from turtle import Turtle

level_array = []


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("black")
        self.level = 0
        self.hideturtle()

    def updateScore(self):
        self.write(f"Level : {self.level}", align="center", font=("arial", 24, "normal"))

    def increase_Score(self):
        self.level += 1
        print(self.level)
        self.clear()
        self.updateScore()

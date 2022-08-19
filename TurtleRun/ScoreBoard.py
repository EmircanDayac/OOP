from turtle import Turtle



class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("Black")
        self.level = 0
        self.penup()
        self.hideturtle()



    def increase_Score(self):
        self.level+=10
        self.clear()
        self.updateScore()

    def updateScore(self):
        self.write(f"Score : {self.level}", align="center", font=("arial", 24, "normal"))




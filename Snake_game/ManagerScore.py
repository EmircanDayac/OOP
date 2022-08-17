from turtle import Turtle



class ManagerScore(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        self.penup()
        self.hideturtle()



    def increase_Score(self):
        self.score+=10
        self.clear()
        self.updateScore()

    def updateScore(self):
        self.write(f"Score : {self.score}", align="center", font=("arial", 24, "normal"))




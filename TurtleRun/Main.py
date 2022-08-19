from turtle import Turtle, Screen
from Player import Player
from CarManager import CarManager

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("white")
screen.title("Turtle-Run")
Player()
CarManager()

if Player().turtle_list[0].distance(CarManager.Cars):
    print("gir2")
    Turtle.write(f"Game Over", align="center", font=("arial", 24, "normal"))

screen.exitonclick()

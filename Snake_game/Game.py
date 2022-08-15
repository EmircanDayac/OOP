import time
from turtle import Turtle, Screen

screen = Screen()
screen.setup(600, 600)
screen.listen()
position = [(0, 0), (-20, 0), (-40, 0)]

screen.title("Snake-Game")

snakes_component = []
for i in position:
    snake = Turtle()
    snake.penup()
    screen.bgcolor("black")
    snake.color("white")
    snake.shape("square")
    snake.goto(i)
    snakes_component.append(snake)

isalive = True


def snake_forward():
    while isalive:
        screen.update()
        time.sleep(0.1)
        for seg_num in range(len(snakes_component) -1 ,0,-1):
            new_x = snakes_component[seg_num - 1].xcor()
            new_y = snakes_component[seg_num - 1].ycor()
            snakes_component[seg_num].goto(new_x,new_y)
            snakes_component[0].forward(10)

def up():
    snakes_component[0].setheading(90)


def down():
    snakes_component[0].setheading(270)

def left():
    snakes_component[0].setheading(180)


def right():
    snakes_component[0].setheading(0)


screen.onkey(up,"Up")
screen.onkey(down,"Down")
screen.onkey(left,"Left")
screen.onkey(right,"Right")




snake_forward()

screen.exitonclick()

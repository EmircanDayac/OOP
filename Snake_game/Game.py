import random
import time
from turtle import Turtle, Screen
from food import food
from ManagerScore import ManagerScore
Y = ManagerScore()






screen = Screen()
screen.setup(600, 600)
screen.listen()
position = [(0, 0), (-20, 0), (-40, 0)]
d = food()
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

position2 = [100,200,-100,-200]
a = random.choice(position2)
b = random.choice(position2)
def snake_forward(i=2):
    while isalive:
        screen.update()
        time.sleep(0.1)
        for seg_num in range(len(snakes_component) -1 ,0,-1):
            (new_x) = snakes_component[seg_num - 1].xcor()
            new_y = snakes_component[seg_num - 1].ycor()
            snakes_component[seg_num].goto(new_x,new_y)
            snakes_component[0].forward(10)
            print(snakes_component[0].xcor())
            #Collision için iyi bir mantık
            if snakes_component[0].distance(d) < 15:
              print("Ayşşemin Mamağı")
              d.goto(random.choice(position2),random.choice(position2))
              c =  position[i][0]
              i+=1
              print(i)
              position.append((c-20,0))
              print(position)
              Y.increase_Score()





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

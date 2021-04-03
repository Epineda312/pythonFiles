from turtle import Screen, Turtle
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()



























# segment_1 = Turtle("square")
# segment_1.color("white")
#
# segment_2 = Turtle("square")
# segment_2.color("white")
# segment_2.goto(x=-20, y=0)
#
# segment_3 = Turtle("square")
# segment_3.color("white")
# segment_3.goto(x=20, y=0)


# tim = Turtle("square")
# tim.color("white")
# # y_positions = [-20, 0, 20]
# x_positions = [-20, 0, 20]
#
# for turtle_index in range(0, 3):
#     new_turtle = Turtle(shape="square")
#     new_turtle.penup()
#     new_turtle.color("white")
#     new_turtle.goto(x=x_positions[turtle_index], y=0)
#













screen.exitonclick()
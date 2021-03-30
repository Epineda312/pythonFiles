from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

starting_positions = [(0, 0), (-20, 0), (-40, 0)]

segments = []


for position in  starting_positions:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)

game_is_on = True

while game_is_on:
    for seg in segments:
        seg.pen()
        seg.forward(20)

























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
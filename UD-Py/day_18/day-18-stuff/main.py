import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
tim.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)


def random_walk():
    for _ in range(200):
        tim.color(random_color())
        tim.forward(30)
        tim.setheading(random.choice(directions))

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

# colors = ["Black", "Red", "CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat",
#           "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]
tim.pensize(3)
tim.shape("turtle")

# control tim
draw_spirograph(5)








screen = t.Screen()
screen.exitonclick()

# def square():
#     for _ in range(4):
#         tim.forward(100)
#         tim.right(90)
#
#
# def dotted_line():
#     for _ in range(10):
#         tim.forward(10)
#         tim.penup()
#         tim.forward(10)
#         tim.pendown()
#

# def triangle():
#     for _ in range(3):
#         tim.forward(100)
#         tim.right(120)
#
#
# def pentagon():
#     for _ in range(5):
#         tim.forward(100)
#         tim.right(72)
#
#
# def hexagon():
#     for _ in range(6):
#         tim.forward(100)
#         tim.right(60)
#
#
# def heptagon():
#     for _ in range(7):
#         tim.forward(100)
#         tim.right(51.43)
#
#
# def octagon():
#     for _ in range(8):
#         tim.forward(100)
#         tim.right(45)
#
#
# def nonagon():
#     for _ in range(9):
#         tim.forward(100)
#         tim.right(40)
#
#
# def decagon():
#     for _ in range(10):
#         tim.forward(100)
#         tim.right(36)
#

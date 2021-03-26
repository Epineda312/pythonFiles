# # import colorgram
# # rgb_colors = []
# # colors = colorgram.extract('image.jpeg', 10)
# #
# # for color in colors:
# #     # rgb = (color.rgb.r, color.rgb.g, color.rgb.b)
# #     r = color.rgb.r
# #     b = color.rgb.b
# #     g = color.rgb.g
# #     new_color = (r, b, g)
# #     rgb_colors.append(new_color)
# #
# # print(rgb_colors)


# # 10 x 10
# # dots 20 in size, spaced by 50
# # use colors from image
import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(239, 231, 214), (225, 158, 68), (235, 238, 245), (244, 233, 239), (50, 96, 57), (61, 121, 171),
              (240, 201, 60), (236, 244, 239), (221, 172, 199)]

tim.setheading(225)
tim.forward(250)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.penup()
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()

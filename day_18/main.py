# import colorgram
from random import choice
from turtle import Turtle, Screen, colormode
from tk_colors import rdm_rgb_color

# colours = colorgram.extract('playa.jpg', 30)
# rgb_colours = []
#
# for colour in colours:
#     r = colour.rgb.r
#     g = colour.rgb.g
#     b = colour.rgb.b
#     new_colour = (r, g, b)
#     rgb_colours.append(new_colour)

colours = [(131, 166, 211), (156, 189, 235), (105, 92, 74), (44, 35, 25), (169, 204, 245), (32, 32, 41), (36, 29, 34), (160, 145, 127), (97, 88, 94), (87, 89, 103), (105, 125, 164), (77, 70, 39), (144, 133, 97), (148, 139, 145), (28, 31, 29), (59, 60, 73), (76, 58, 53), (69, 60, 65), (133, 123, 129), (139, 123, 119), (86, 90, 87), (221, 202, 189), (223, 215, 221), (145, 149, 147), (220, 192, 152), (203, 187, 183), (199, 186, 190), (61, 67, 59), (123, 129, 128), (57, 66, 69)]

tim = Turtle()
tim.penup()
tim.hideturtle()
tim.speed(10)
colormode(255)

def dot():
    colour = rdm_rgb_color("b", 255)
    tim.dot(20, colour); tim.fd(50)

def line(length):
    for _ in range(0, length):
        dot()

def canvas(lines, dots):
    tim.goto(-200, -200)
    for _ in range(0, lines):
        line(dots)
        tim.backward(50 * dots)
        tim.left(90)
        tim.fd(50)
        tim.setheading(0)


canvas(10, 10)


screen = Screen()
screen.exitonclick()

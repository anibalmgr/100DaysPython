from random import randint, choice
from turtle import Turtle, Screen, colormode
from tk_colors import COLORS, rdm_rgb_color


tim = Turtle()
tim.shape("turtle")
tim.color("aquamarine")
tim.speed(10)
colormode(255)


def start():
    tim.home()
    tim.clear()
    tim.pendown()
    tim.pensize(8)
    tim.pencolor(rdm_rgb_color("b"))
# Challenge 1:


def square(size):
    start()
    for _ in range(0, 4):
        tim.forward(size)
        tim.right(90)

# challenge 2: draw a dotted line.


def dotted_line(length):
    start()
    if length > 100:
        tim.pensize(10)
    else:
        tim.pensize(round(length / 10))
    for _ in range(0, length):
        if _ % 2 == 0:
            tim.pendown()
        else:
            tim.penup()
        tim.forward(length / 4)

# Challenge 3:


def draw_shape(sides):
    deg = 360 / sides
    for side in range(0, sides):
        tim.forward(40)
        tim.right(deg)


def shapes(number):
    start()
    for sides in range(3, number):
        draw_shape(sides)
        tim.color(choice(COLORS))


# Challenge 4. random walk:

def random_step():
    direction = randint(0, 3) * 90
    tim.pencolor(rdm_rgb_color("g", 250))
    tim.forward(30)
    tim.setheading(direction)


def rdm_walk(steps):
    start()
    tim.pensize(8)
    for _ in range(0, steps):
        random_step()

# draw a spirograph


def spiro(circles):
    start()
    tim.pensize(2)
    for circle in range(circles):
        tim.pencolor(rdm_rgb_color("r", 200))
        tim.circle(100)
        tim.left(360/circles)

spiro(5)
rdm_walk(50)
shapes(11)
dotted_line(100)
square(100)

screen = Screen()
screen.exitonclick()
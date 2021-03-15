from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

is_race_on = False

all_turtles = []

for turtle in colors:
    number = colors.index(turtle)
    position_y = number * 50 - 100
    turtle = Turtle(shape="turtle")
    turtle.color(colors[number])
    turtle.penup()
    turtle.goto(x=-230, y=position_y)
    all_turtles.append(turtle)

if user_bet:
    is_race_on = True


while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() < 230:
            rand_distance = random.randint(0, 10)
            turtle.forward(rand_distance)
        else:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've bet {winning_color}, you won!")
            else:
                print(f"The winner is {winning_color}, you've lost!")
            is_race_on = False


screen.exitonclick()

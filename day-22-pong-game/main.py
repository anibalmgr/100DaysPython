from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

player1 = Paddle("player1")
player2 = Paddle("player2")
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player1.go_up, "w")
screen.onkeypress(player1.go_down, "s")
screen.onkeypress(player2.go_up, "Up")
screen.onkeypress(player2.go_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # collision with top and bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Collision with paddles
    if ball.xcor() == 330 and ball.distance(player2) < 70:
        ball.bounce_x()

    if ball.xcor() == -330 and ball.distance(player1) < 70:
        ball.bounce_x()

    # Detect if a player misses the ball
    if ball.xcor() > 410:
        ball.reset_position()
        scoreboard.point_1()

    if ball.xcor() < -410:
        ball.reset_position()
        scoreboard.point_2()

screen.exitonclick()

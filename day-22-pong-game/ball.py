from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.dir_y = 15
        self.dir_x = 15
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.dir_x
        new_y = self.ycor() + self.dir_y
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.dir_y *= -1

    def bounce_x(self):
        self.dir_x *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.dir_x *= -1
        self.goto(0, 0)
        self.move_speed = 0.1
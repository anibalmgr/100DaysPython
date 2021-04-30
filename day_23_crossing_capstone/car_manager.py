from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = -5
MOVE_INCREMENT = -5


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.speed = STARTING_MOVE_DISTANCE
        self.random_range = 60

    def create_car(self):
        random_chance = random.randint(1, self.random_range)
        if 1 <= random_chance < 10:
            new_car = Turtle()
            new_car.shape("turtle")
            new_car.shapesize(1, 2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.setheading(180)
            random_y = random.randint(-240, 240)
            new_car.goto(320, random_y)
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            self_y = car.ycor()
            new_x = car.xcor() + self.speed
            car.goto(new_x, self_y)

    def increase_speed(self):
        self.speed = self.speed + MOVE_INCREMENT
        if self.random_range > 20:
            self.random_range = self.random_range - 2

    def reset_manager(self):
        for car in self.all_cars:
            car.clear()
        self.all_cars = []
        self.speed = STARTING_MOVE_DISTANCE

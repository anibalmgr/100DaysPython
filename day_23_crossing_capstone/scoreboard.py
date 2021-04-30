from turtle import Turtle

FONT = ("Courier", 24, "normal")
INITIAL_SCORE = 0
INITIAL_POSITION = (-200, 240)


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(INITIAL_POSITION)
        self.color("white")
        self.hideturtle()
        self.score = INITIAL_SCORE
        self.update()

    def update(self):
        self.clear()
        self.write(f"SCORE: {self.score}", align="center", font=("Courier", 25, "bold"))

    def point(self):
        self.score += 1
        self.update()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Impact", 60, "bold"))
        self.goto(0, -30)
        self.write(f"Your score is: {self.score}", align="center", font=("Times", 20, "bold"))
        self.goto(0, -60)
        self.write("Do you want to try again? y", align="center", font=("Times", 15, "normal"))

    def reset_scoreboard(self):
        self.clear()
        self.goto(INITIAL_POSITION)
        self.score = INITIAL_SCORE
        self.update()
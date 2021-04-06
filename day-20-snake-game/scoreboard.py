from turtle import Turtle

ALIGN= "center"
FONT = ("Courier new", 16, "normal")

class Board(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        self.speed("fastest")
        self.penup()
        self.pencolor("white")
        self.goto(-0, 270)
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)

    def gameover(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGN, font=FONT)

    def update_board(self):
        self.score += 1
        self.clear()
        self.update_score()
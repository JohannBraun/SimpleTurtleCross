from turtle import Turtle

FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-280, 260)
        self.color("black")

    def refresh(self, turtle):
        self.clear()
        self.write(f"Level: {turtle.score}", align="left", font=FONT)

    def you_lose(self, turtle):
        self.clear()
        self.goto(0, 0)
        self.write(f"You lose! Final score: {turtle.score}", align="center",font=FONT)

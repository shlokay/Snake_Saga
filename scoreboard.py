import turtle
from turtle import Turtle, Screen
from snake import Snake
from food import Food


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()

    def update_score(self):
        self.goto(0, 260)
        self.write(f"Score : {self.score}", move=False, align="center", font=("Arial", 24, "bold"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.color("white")
        self.update_score()

    def crashed(self):
        self.clear()
        self.color("red")
        self.penup()
        self.goto(0, 35)
        self.write("CRASHED", move= False, align="center", font=("Arial", 35, "bold") )
        self.goto(0, 0)
        self.color("white")
        self.write(f"Score : {self.score}", move=False, align="center", font=("Arial", 24, "bold"))

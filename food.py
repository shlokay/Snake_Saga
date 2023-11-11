from turtle import Turtle
import random
from snake import Snake
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.4, stretch_wid=0.4)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        xcor = random.randint(-270, 270)
        ycor = random.randint(-270, 270)
        self.goto(xcor, ycor)



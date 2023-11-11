import turtle
from turtle import Turtle, Screen
import time
from food import Food
food = Food()
from snake import Snake
from scoreboard import Scoreboard

scoreboard = Scoreboard()
screen = Screen()
snake = Snake()

screen.title("SNAKE SAGA")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)



is_game_on = True




screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.right, "d")
screen.onkey(snake.left, "a")


score = 0
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move_forward()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

     # Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.ycor() > 290:
        scoreboard.crashed()
        is_game_on = False
    elif snake.head.xcor() < -290 or snake.head.ycor()< -290:
        scoreboard.crashed()
        is_game_on = False

#   Checking whether snake hit its tail or not:
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 1:
            scoreboard.crashed()
            is_game_on = False





screen.exitonclick()

from turtle import Screen
from turtle import Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from ui import User_Interface








interface = User_Interface()
snake = Snake()
i = Food()
scoreboard = Scoreboard()
while interface.game_on:
    screen = Screen()
    screen.setup(width=600, height=600)





    screen.bgcolor("red")
    screen.title("My Snake Game")



    screen.tracer(0)
    screen.update()

    time.sleep(.1)
    snake.move()

    screen.listen()

    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.right, "Right")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.spin, "space")

    if snake.head.distance(i) <15:


        i.refresh()
        scoreboard.update_score()
        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() >280 or snake.head.ycor() < -280:
            game_on = False
            scoreboard.game_over()


































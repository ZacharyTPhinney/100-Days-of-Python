from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.bgcolor("orange")
screen.title("My Snake Game")
screen.tracer(0)
screen.setup(width=600,height=600)



snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")


game_on = True

while game_on :
    screen.update()
    time.sleep(.1)
    snake.move()
    if snake.head.distance(food) <15:
        food.refresh()

        scoreboard.update_score()
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() >280 or snake.head.ycor() < -280:
        game_on = False
        scoreboard.game_over()

































screen.exitonclick()

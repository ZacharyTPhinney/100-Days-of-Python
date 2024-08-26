from turtle import Screen,Turtle
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
snake = Turtle()
snakes=[]
x=0
for i in range(3):



    snake.shape("square")
    snake.color("white")

    x = x - 20
    snake.goto(x,0)
    snakes.append(snake)
for snake in snakes:
    


screen.exitonclick()
from turtle import Turtle,Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet=screen.textinput(title= "Make your bet", prompt="Which turtle will win the race? Enter a color")
y=0
colors=["red","blue","red","orange","purple","pink"]
all_turtles=[]
for i in range(0,6):
    y+=10
    new_turtle = Turtle()
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y)
    new_turtle.color(colors[i-1])
    all_turtles.append(new_turtle)
if user_bet:
    race=True

while race:
    for turtle in all_turtles:
        if turtle.xcor()>230:
            race=False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won {winning_color} turtle is the winner" )
            else:
                print(f"You've lost The {winning_color} is the winner")
        rand_distance=random.randint(0,10)
        turtle.forward(rand_distance)
screen.exitonclick()
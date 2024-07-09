from turtle import Turtle,Screen


screen = Screen()
screen.setup(width=500, height=400)
user_bet=screen.textinput(title= "Make your bet", prompt="Which turtle will win the race? Enter a color")
tim = Turtle()
tim.penup()
tim.goto(x=-230,y=0)
tim.color("green")

charles=Turtle()
charles.color("red")
charles.goto(x=-230,y=40)

stacy = Turtle()
stacy.color("pink")
stacy.goto(x=-230,y=80)

Chaz =Turtle()
Chaz.goto(x=-230,y=120)
Chaz.color("yellow")

Brenda = Turtle()
Brenda.color("blue")
Brenda.goto(x=-230, y=160)

Brenda = Turtle()
Brenda.color("orange")
Brenda.goto(x=-230,y=200)

screen.exitonclick()
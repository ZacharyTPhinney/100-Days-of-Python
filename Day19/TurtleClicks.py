from  turtle import Turtle,Screen
tim =  Turtle()
screen = Screen()

def move_forward():
    tim.setheading(0)
    tim.forward(100)
def move_backward():
    tim.setheading(180)
    tim.forward(100)
def move_right():
    tim.setheading(270)
    tim.forward(100)
def move_left():
    tim.setheading(90)
    tim.forward(100)
def clear():
    tim.clear()
    tim.penup()
    tim.setx(0)
    tim.sety(0)
    tim.pendown()



screen.listen()
screen.onkey(move_forward,"w")
screen.onkey(move_backward,"s")
screen.onkey(move_right,"p")
screen.onkey(move_left,"l")
screen.onkey(clear,"c")


screen.exitonclick()
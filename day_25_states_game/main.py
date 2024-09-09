from turtle import Turtle
import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
states_left = 50
while states_left <= 50:
    answer_state = screen.textinput(title="Guess the State",prompt = "What's another state's name?")
    coordinates=pandas.read_csv("50_states.csv")
    coordinates =coordinates.to_dict()
    for i in range(50):
        if coordinates['state'][i] == answer_state:
            x =coordinates['x'][i]
            y =  coordinates['y'][i]
            state = coordinates['state'][i]


            new_turtle = Turtle()
            new_turtle.penup()
            new_turtle.setx(x)
            new_turtle.sety(y)
            new_turtle.hideturtle()

            new_turtle.write(f"{state}")
            print(coordinates)
            states_left -=1


screen.exitonclick()
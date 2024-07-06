from turtle import Turtle,Screen
import random
timmy = Turtle()
colours=["Gold","red","blue","purple","orange"]
def draw_shape(num_sides):
    angle= 360/num_sides
    for i in range(num_sides):

        timmy.forward(100)
        timmy.right(angle)

for shape_side_n in range(3,11):
    timmy.color(random.choice(colours))
    draw_shape(shape_side_n)

screen=Screen()
screen.exitonclick()
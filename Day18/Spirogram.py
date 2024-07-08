import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

########### Challenge 5 - Spirograph ########
tim.speed("fastest")
for i in range(50):
    
    tim.circle(100)
    tim.shapesize(5,5)
    tim.forward(1)
    tim.color(random_color())
    tim.left(10)
    tim.tilt(45)


    
    

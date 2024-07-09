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
    import colorgram 
    colors = colorgram.extract('image.webp',6)
    rgbcolors = [(249, 248, 244), (250, 245, 248), (243, 250, 246), (236, 244, 250), (236, 224, 80), (197, 7, 71), (195, 164, 13),(201, 75, 15), (231, 54, 132), (110, 179, 216), (217, 163, 101), (27, 105, 168), (35, 186, 109), (19, 29, 168),(13, 23, 66), (212, 135, 177), (233, 223, 7), (199, 33, 132), (13, 183, 212), (230, 166, 199), (126, 189, 162),(8, 49, 28), (40, 132, 77), (128, 219, 232), (58, 12, 25), (67, 22, 7), (114, 90, 210), (146, 216, 199),(179, 17, 8), (233, 66, 34)]

########### Challenge 5 - Spirograph ########
tim.speed("fastest")
j = 0
while j > -250:
    tim.setx(-50)
    for i in range(10):

        tim.dot(20,random_color())
        
        tim.penup()
        tim.forward(50)


        tim.dot(20)
    j = j - 25
    tim.sety(j)
    print(j)
tim.screen.exitonclick()



    
    

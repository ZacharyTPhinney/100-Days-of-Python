from turtle import Turtle
import turtle
import random
from turtle import Screen
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.image = 'chaos_emeraldd.gif'
        win = Screen()
        win.register_shape(self.image)
        self.shape(self.image)





        self.penup()
        # self.shapesize(stretch_len=.5, stretch_wid=.5)
        # self.color("blue")
        # self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-200, 280)
        random_y = random.randint(-200, 280)
        self.goto(random_x,random_y)
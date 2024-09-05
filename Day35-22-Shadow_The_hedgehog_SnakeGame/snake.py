from turtle import Turtle
import tkinter as tk
from tkinter import PhotoImage
from turtle import Screen

POSITIONS = [(0, 0), (20, 0), (40, 0)]


class Snake:

    def __init__(self):
        self.snakes = []
        self.create_snake()
        self.head = self.snakes[0]


    def create_snake(self):

        # for position in POSITIONS:

            # new_snake = Turtle("square")
            # new_snake.color("red")
            # new_snake.penup()
            # new_snake.goto(position)
            # self.snakes.append(new_snake)

        self.sprite = Turtle()
        win = Screen()
        win.register_shape('shadow_giff.gif')

        self.sprite.shape('shadow_giff.gif')
        self.snakes.append(self.sprite)
        self.sprite.penup()




    def move(self):
        for seg_num in range(len(self.snakes) - 1, 0, -1):
            new_x = self.snakes[seg_num - 1].xcor()
            new_y = self.snakes[seg_num - 1].ycor()
            self.snakes[seg_num].goto(new_x, new_y)
        self.snakes[0].forward(15)

    def right(self):
        self.snakes[0].setheading(0)


    def left(self):

        self.snakes[0].setheading(180)


    def down(self):
        self.snakes[0].setheading(270)

    def up(self):
        self.snakes[0].setheading(90)
    def spin(self):
        for i in range(6):

            self.sprite.left(10)
            self.sprite.tilt(180)

            self.sprite.right(60)



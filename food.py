from turtle import Turtle
from random import randint


class Snake_food(Turtle):
    def __init__(self):
        super().__init__() #super class (Turtle) init method
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.random_refresh()
        
    def random_refresh(self):
        x_random = randint(-280, 280)
        y_random = randint(-230, 230)
        self.goto(x_random, y_random)

        
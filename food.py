from turtle import Turtle
import random as r

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color('red')
        self.speed("fastest")
        self.refresh()
    def refresh(self):
        self.goto(x=r.randint(-280,280),y=r.randint(-280,280))


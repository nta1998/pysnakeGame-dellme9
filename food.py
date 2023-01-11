from turtle import Turtle
import turtle
import random

class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5,0.5)
        self.color("dark olive green")
        self.speed("fastest")
        self.refresh()
    
    def refresh(self):
        x = random.randint(-350,350)
        y = random.randint(-350,350)
        self.goto(x,y)
        
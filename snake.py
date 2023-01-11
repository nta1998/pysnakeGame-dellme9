import random
from turtle import Turtle
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
posi = [(0,0),(-20,0),(-40,0)]
class Snake:
    
    def __init__(self):
        self.body = []
        self.create_snake()
        self.head = self.body[0]
    
    
    def create_snake(self):
        for pos in posi:
            self.add(pos)
    
    def add(self,pos):
        co = ["dark green","green","green yellow","chartreuse","dark olive green"]
        new = Turtle()
        new.shape("square")
        new.color(random.choice(co))
        new.penup()
        new.goto(pos)
        self.body.append(new)
     
    def add_f(self):
        self.add(self.body[-1].position())
    def move(self):
        for num in range(len(self.body) -1,0,-1):
            x = self.body[num -1].xcor()
            y = self.body[num -1].ycor()
            self.body[num].goto(x,y)
        self.body[0].forward(20)
    
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
        
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
       
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    
    def agin(self):
        for part in self.body:
            part.goto(1000,1000)
        self.body.clear()
        self.create_snake()
        self.head = self.body[0]
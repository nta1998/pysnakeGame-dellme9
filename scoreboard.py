from turtle import Turtle

class Scorebord(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.higest_score = int(data.read())     
        self.penup()
        self.color("white")
        self.goto(0,350)
        self.score_in()
        self.hideturtle()
    def score_in(self):
        self.clear()
        self.write(f"score: {self.score} high score: {self.higest_score}",align = "center",font = ("Arial",24, "normal"))
    
    
    def inscore(self):
        self.score += 1
        self.clear()
        self.score_in()
    def resat(self):
        if self.score > self.higest_score:
            self.higest_score = self.score
            with open("data.txt", mode= "w") as data:
                data.write(f"{self.score}")
        self.score = 0 
        self.score_in()    
    # def game_over(self):
    #     self.penup()
    #     self.color("red")
    #     self.goto(0,0)      
    #     self.write(f"GAME OVER",align = "center",font = ("Arial",24, "normal"))
        
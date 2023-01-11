from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scorebord
screen = Screen()
screen.setup(800,800)
screen.bgcolor("black")
screen.tracer(0)
screen.title(" liloz snake Game ")

snake = Snake()
food = Food()
scorebord = Scorebord()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on =True    
while game_is_on:
    screen.update()
    time.sleep(0.1)  
    snake.move()
    
    if snake.head.distance(food) < 15:
        food.refresh()
        scorebord.inscore()
        snake.add_f()
    if snake.head.xcor() > 390 or snake.head.xcor() < -390 or snake.head.ycor() > 390 or snake.head.ycor() < -390:
        scorebord.resat()
        snake.agin()
    

    for seg in snake.body[2:]:
        if snake.head.distance(seg) < 15:
            scorebord.resat()
            snake.agin()
        






















screen.exitonclick()
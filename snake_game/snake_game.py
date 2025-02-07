from turtle import Turtle,colormode,Screen
import time
import random

colormode(255)
myscreen = Screen()
myscreen.setup(700,500)
myscreen.bgcolor("black")

snake = Turtle("square")
snake.color(64, 161, 58)
snake.shapesize(None ,5,2)
snake.penup()
snake.speed(1)

mouse = Turtle()
mouse.color(64, 43, 69)
mouse.penup()
mouse.goto(random.randint(-300,300),random.randint(-300,300))

def l():
    x = snake.heading()
    snake.setheading(x + 90)
def r():
    x = snake.heading()
    snake.setheading(x - 90)

def c():
    snake.clear()
    snake.home()

myscreen.listen()    
myscreen.onkey(key = "a",fun = l)
myscreen.onkey(key = "d",fun = r)
myscreen.onkey(key = "c",fun = c)


uncrashed =  True
while uncrashed:
    
    snake.forward(5)
    time.sleep(0.1)
    y = snake.ycor()
    x = snake.xcor()
    if -300 > x or x > 300  or y < -200 or y > 200:
        uncrashed = False
        print("CRASHED")
        


    




    
    
myscreen.exitonclick()

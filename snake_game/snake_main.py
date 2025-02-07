from turtle import Turtle,colormode,Screen,bye
from snake import Snake
import random
import time

colormode(255)
myscreen = Screen()
myscreen.setup(700,500)
myscreen.bgcolor("black")
myscreen.tracer(0)

from food import mouse
snake = Snake()

myscreen.listen()    
myscreen.onkey(lambda: snake.move("up"), key="Up")
myscreen.onkey(lambda: snake.move("down"), key="Down")
myscreen.onkey(lambda: snake.move("left"), key="Left")
myscreen.onkey(lambda: snake.move("right"), key="Right")
myscreen.onkey(bye , key= "0")

uncrashed =  True
while uncrashed:
    myscreen.update()
    time.sleep(0.5)
    if snake.working(myscreen.window_width(),myscreen.window_height()) == False:
        uncrashed = False
        myscreen.update()
    
myscreen.exitonclick()
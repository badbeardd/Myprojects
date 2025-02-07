from turtle import Turtle
import food
import random
from snake_score import Scoreboard

class Snake:
    
    def __init__(self):
        self.list = []
        self.body_behind = 0
        self.create_snake()
        self.score = 0
        self.scoreboard = Scoreboard()

    def create_snake(self):
        for self.i in range(3):
            
            snake = Turtle("square")
            #snake.shapesize(None,1,None)
            if self.i == 0:
                snake.color(197, 22, 41)
            else:    
                snake.color(64, 161, 58)
            snake.penup()
            snake.speed("fastest")
            snake.goto(self.body_behind,0)
            self.body_behind = int(snake.xcor()-20)
            self.list.append(snake)
            


    def move(self,key):
        if key == "up":
            if self.list[0].heading() != 270 :
                self.list[0].setheading(90)

        if key == "down":
            if self.list[0].heading() != 90:
                self.list[0].setheading(270)

        if key == "left":
            self.list[0].setheading(self.list[0].heading() + 90)
         
        if key == "right":
            self.list[0].setheading(self.list[0].heading() - 90)


    def working(self,width,height):
                
        for j in range(len(self.list)-1,0,-1):
            self.list[len(self.list)-1].color(64,161,58)
            new_x = self.list[j-1].xcor()
            new_y = self.list[j-1].ycor()
            self.list[j].goto(new_x,new_y)
        self.list[0].forward(20)
        y = self.list[0].ycor()
        x = self.list[0].xcor()
        if x - 10 <= food.mouse.xcor() <= x + 10 and  y - 10 <= food.mouse.ycor() <= y + 10:
            snake = Turtle("square")
            snake.penup()
            self.list.append(snake)
            food.mouse.goto(random.randint(-300,300),random.randint(-200,200))
            self.scoreboard.increase_score()
            #print(self.score)
        if -(width/2) > x-20 or x+20 > (width/2)  or y < -(height/2) or y > (height/2) :
            self.scoreboard.game_over()
            return False
        for i in range(1,len(self.list),1):
            if self.list[i].xcor() - 10 < x < self.list[i].xcor() + 10 and self.list[i].ycor() - 10 < y < self.list[i].ycor() + 10:
                self.scoreboard.game_over()
                return False

        




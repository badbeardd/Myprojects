from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        self.penup()
        self.goto(0,190)
        self.write(f"Score:{self.score}",align = "center",font =("Arial",24,"normal"))
        self.hideturtle()
        
    def game_over(self):
        self.goto(0,0)
        self.write("Game over",align = "center",font =("Arial",24,"normal"))
        
    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score:{self.score}",align = "center",font =("Arial",24,"normal"))
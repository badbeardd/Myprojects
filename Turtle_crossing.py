**ninja_turtle.py**
from turtle import Turtle, Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import time
import random

# Screen setup
myscreen = Screen()
myscreen.setup(width=600, height=600)
myscreen.bgcolor("black")
myscreen.tracer(0)

# Create game objects
ninja_turtle = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

# Control setup
myscreen.listen()
myscreen.onkey(ninja_turtle.player_move, key="Up")

# Main game loop
is_game_on = True
while is_game_on:
    time.sleep(0.1)
    myscreen.update()

    # Create and move cars
    car_manager.create_cars()
    car_manager.move_cars()

    # Detect collision with cars
    for car in car_manager.all_cars:
        if ninja_turtle.distance(car) < 20:
            is_game_on = False
            scoreboard.game_over()

    # Check if player reaches the finish line
    if ninja_turtle.ycor() > 280:
        ninja_turtle.reset_position()
        car_manager.level_up()
        scoreboard.increase_level()

myscreen.exitonclick()
```

**player.py**
from turtle import Turtle

CAR_FINISH = 280
INCREMENT = 10
STARTING_POSITION = (0, -280)

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("white")
        self.penup()
        self.setheading(90)
        self.reset_position()

    def player_move(self):
        if self.ycor() < CAR_FINISH:
            self.forward(INCREMENT)

    def reset_position(self):
        self.goto(STARTING_POSITION)
```

**scoreboard.py**
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(-270, 265)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=("Arial", 24, "normal"))

    def game_over(self):
        self.goto(-100, 0)
        self.write("GAME OVER", align="center", font=("Arial", 24, "normal"))

    def increase_level(self):
        self.level += 1
        self.update_score()
```

**car_manager.py**
from turtle import Turtle
import random

CAR_COLORS = ["red", "green", "blue", "orange", "purple", "yellow"]
STARTING_CAR_SPEED = 5
SPEED_INCREMENT = 10

class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_CAR_SPEED

    def create_cars(self):
        # Create new cars with a 1 in 6 chance per frame
        if random.randint(1, 6) == 1:
            car = Turtle("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            car.color(random.choice(CAR_COLORS))
            random_y = random.randint(-250, 250)
            car.goto(300, random_y)
            self.all_cars.append(car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += SPEED_INCREMENT

from turtle import Turtle, Screen
import time

# Constants
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
PADDLE_SPEED = 20
BALL_SPEED = 2
MAX_SCORE = 10

class Paddle(Turtle):
    def __init__(self, x_pos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x_pos, 0)

    def move_up(self):
        if self.ycor() < 200:
            self.sety(self.ycor() + PADDLE_SPEED)

    def move_down(self):
        if self.ycor() > -200:
            self.sety(self.ycor() - PADDLE_SPEED)

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.dx = BALL_SPEED
        self.dy = BALL_SPEED
        self.speed_increase_count = 0

    def move(self):
        self.setx(self.xcor() + self.dx)
        self.sety(self.ycor() + self.dy)

    def bounce_y(self):
        self.dy *= -1

    def bounce_x(self):
        self.dx *= -1
        self.speed_increase_count += 1
        if self.speed_increase_count % 5 == 0:
            self.dx *= 1.1
            self.dy *= 1.1

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-50, 200)
        self.write(self.l_score, align="center", font=("Arial", 24, "normal"))
        self.goto(50, 200)
        self.write(self.r_score, align="center", font=("Arial", 24, "normal"))

    def increase_left(self):
        self.l_score += 1
        self.update_scoreboard()

    def increase_right(self):
        self.r_score += 1
        self.update_scoreboard()

def game_over(winner):
    scoreboard.clear()
    scoreboard.goto(0, 0)
    scoreboard.write(f"Game Over! {winner} Wins", align="center", font=("Arial", 24, "bold"))
    screen.update()
    time.sleep(3)
    screen.bye()

# Setup screen
screen = Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.bgcolor("black")
screen.tracer(0)

# Create paddles, ball, and scoreboard
left_paddle = Paddle(-330)
right_paddle = Paddle(330)
ball = Ball()
scoreboard = Scoreboard()

# Controls
screen.listen()
screen.onkeypress(left_paddle.move_up, "w")
screen.onkeypress(left_paddle.move_down, "s")
screen.onkeypress(right_paddle.move_up, "Up")
screen.onkeypress(right_paddle.move_down, "Down")

# Game loop
while True:
    screen.update()
    time.sleep(0.01)
    ball.move()

    # Bounce off top and bottom walls
    if abs(ball.ycor()) > 240:
        ball.bounce_y()

    # Paddle collision
    if ball.xcor() > 310 and ball.distance(right_paddle) < 50:
        ball.bounce_x()
    elif ball.xcor() < -310 and ball.distance(left_paddle) < 50:
        ball.bounce_x()

    # Ball out of bounds (scoring)
    if ball.xcor() > 350:
        scoreboard.increase_left()
        ball.reset_position()
    elif ball.xcor() < -350:
        scoreboard.increase_right()
        ball.reset_position()

    # Check for game over
    if scoreboard.l_score == MAX_SCORE:
        game_over("Left Player")
    elif scoreboard.r_score == MAX_SCORE:
        game_over("Right Player")


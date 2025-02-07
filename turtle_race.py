from turtle import Turtle, colormode, Screen
import random

screen = Screen()
colormode(255)

# Setup screen
screen.setup(1000, 700)
screen.bgcolor("lightgreen")  # Set grass-like background color

# Draw finish line
finish_line = Turtle()
finish_line.hideturtle()
finish_line.penup()
finish_line.goto(350, 300)
finish_line.setheading(270)
finish_line.pendown()
finish_line.color("white")
finish_line.width(5)
for _ in range(15):
    finish_line.forward(20)
    finish_line.penup()
    finish_line.forward(20)
    finish_line.pendown()

inputs = screen.textinput("Make Your Bet", "What is your bet color: ")
race_on = False

# Color dictionary
color_dict = {
    "red": (255, 0, 0),
    "orange": (255, 165, 0),
    "yellow": (255, 255, 0),
    "green": (0, 128, 0),
    "blue": (0, 0, 255),
    "indigo": (75, 0, 130),
    "violet": (138, 43, 226)
}

if inputs:
    inputs = inputs.lower()  # Normalize input for case-insensitive comparison
    race_on = True

# Create turtles and position them
all_turtles = []
i = -300

for color_name in color_dict:  # Loop through color names in the dictionary
    turtle = Turtle("turtle")
    turtle.penup()
    turtle.color(color_dict[color_name])  # Access color using name
    turtle.goto(-350, i)
    i += 100
    all_turtles.append((turtle, color_name))

while race_on:
    for turtle, color_name in all_turtles:
        rand_dist = random.randint(0, 10)
        turtle.forward(rand_dist)

        # Check for a winning turtle
        if turtle.xcor() >= 350:
            race_on = False
            winning_color = color_name

            if winning_color.lower() == inputs:
                print(f"You Won! The winning turtle was {winning_color.capitalize()}.")
            else:
                print(f"You Lose! The winning turtle was {winning_color.capitalize()}.")
            break

screen.exitonclick()

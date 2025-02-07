import turtle as t
import random

t.colormode(255)
mouse = t.Turtle("circle")
mouse.shapesize(0.5)
mouse.color(64, 43, 69)
mouse.penup()
mouse.goto(random.randint(-300,300),random.randint(-200,200))
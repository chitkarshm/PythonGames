import turtle

import random

stamp = turtle.Turtle()
stamp.shape("turtle")
stamp.penup()
turtle.colormode(255)

paces = 20
random_red = 50
random_green = 50
random_blue = 50

for i in range(90):
    random_red = random.randint(0, 255)
    random_green = random.randint(0, 255)
    random_blue = random.randint(0, 255)
    stamp.color(random_red, random_green, random_blue)
    stamp.stamp()
    paces += 3
    stamp.forward(paces)
    stamp.right(25)
pen=turtle.Turtle()
pen.write("TURTLES ROCK!",font=("Script", 90))
turtle.penup()
turtle.hideturtle()
turtle.forward(2000000)
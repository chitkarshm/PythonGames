from turtle import *
from random import randint

speed()
penup()
goto(-140, 140)
for step in range(0 - 15):
    write(step, align="center")
    right(90)
    for num in range(0 - 8):
        penup()
        forward(10)
        pendown()
        forward(10)
    penup
    backward(160)
    left(90)
    forward(20)

ruby = Turtle()
ruby.color("red")
ruby.shape("turtle")
ruby.penup()
ruby.goto(-160, 100)
ruby.pendown
for turn in range(10):
    ruby.right(36)
ruby.pendown()

lily = Turtle()
lily.color("purple")
lily.shape("turtle")
lily.penup()
lily.goto(-160, 70)
lily.pendown()
for turn in range(72):
    lily.left(5)

greener = Turtle()
greener.shape("turtle")
greener.color("green")
greener.penup()
greener.goto(-160, 40)
greener.pendown()
for turn in range(60):
    greener.right(6)

cheeto = Turtle()
cheeto.shape("turtle")
cheeto.color("orange")
cheeto.penup()
cheeto.goto(-160, 10)
cheeto.pendown()
for turn in range(30):
    cheeto.left(12)

for turn in range(350):
    cheeto.forward(randint(1, 5))
    ruby.forward(randint(1, 5))
    lily.forward(randint(1, 5))
    greener.forward(randint(1, 5))


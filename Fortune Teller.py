import turtle
import random

pointer = turtle.Turtle()
pointer.turtlesize(3, 3, 2)
pen = turtle.Turtle()
spin_amount = random.randint(1, 360)
pen.penup()

# right
pen.goto(300, -32)
pen.pendown()
pen.write("YES, 100%!!👍💯", font=("Sans", 30))
pen.penup()

# left
pen.goto(-600, -32)
pen.pendown()
pen.write("NO, NEVER!!👎❌", font=("Sans", 30))
pen.penup()

# top
pen.goto(-200, 60)
pen.pendown()
pen.write("UMM, MAYBE?🤔❓", font=("Sans", 30))
pen.penup()

# bottom
pen.goto(-400, -200)
pen.pendown()
pen.write("YES, BUT AFTER 50 YEARS!!👍🕜🕜🕜", font=("Sans", 30))

pen.ht()
pointer.right(spin_amount)
turtle.forward(10000)

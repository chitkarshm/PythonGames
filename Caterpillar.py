import turtle
import time
import random

win = turtle.Screen()
win.title("Caterpillar Game")
win.bgcolor("green")
win.screensize(canvwidth=600, canvheight=600)
win.fullscreen()
win.tracer(0)

outline = turtle.Turtle()
outline.hideturtle()
outline.penup()
outline.goto(-300,300)
outline.pendown()
outline.goto(300,300)
outline.goto(300,-300)
outline.goto(-300,-300)
outline.goto(-300,300)

head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("orange")
head.penup()
head.goto(0, 0)
head.direction = "up" 


food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

score = 0
high_score = 0

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 0)
pen.write("Score: 0  HIGH SCORE: 0", align="center", font=("Courier", 24, "bold"))

segments = []


def up():
    if head.direction != "down":
        head.direction = "up"
def down():
    if head.direction != "up":
        head.direction = "down"
def left():
    if head.direction != "right":
        head.direction = "left"
def right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        head.sety(head.ycor() + 20)
    if head.direction == "down":
        head.sety(head.ycor() - 20)
    if head.direction == "left":
        head.setx(head.xcor() - 20)
    if head.direction == "right":
        head.setx(head.xcor() + 20)

win.listen()
win.onkeypress(up, "Up")
win.onkeypress(down, "Down")
win.onkeypress(left, "Left")
win.onkeypress(right, "Right")

def alternate():
    if len(segments) % 2 == 0:
        return "yellow"
    else:
        return "orange"

while True:
    win.update()
    

    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        pen.clear()
        pen.goto(0, 230)
        pen.write("GAME OVER", align="center", font=("Courier", 36, "bold"))
        time.sleep(2)
        score = 0
        pen.clear
        pen.goto(0, 0)
        pen.write(f"SCORE: {score}  HIGH SCORE: {high_score}", align="center", font=("Courier", 24, "bold"))
        


    if head.distance(food) < 20:
        food.goto(random.randint(-280, 280), random.randint(-280, 280))
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("circle")
        new_segment.color(alternate()) 
        new_segment.penup()
        segments.append(new_segment)
        
        score += 1

        if score > high_score:
            high_score = score
        
        pen.clear()
        pen.write(f"SCORE: {score}  HIGH SCORE: {high_score}", align="center", font=("Courier", 24, "bold"))

    for i in range(len(segments) - 1, 0, -1):
        x = segments[i-1].xcor()
        y = segments[i-1].ycor()
        segments[i].goto(x, y)

    if len(segments) > 0:
        segments[0].goto(head.xcor(), head.ycor())

    move()

    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            for s in segments:
                s.goto(1000, 1000)
            segments.clear()
            pen.clear()
            pen.goto(0, 230)
            pen.write("GAME OVER", align="center", font=("Courier", 36, "bold"))
            time.sleep(2)
            score = 0
            pen.clear
            pen.goto(0, 0)
            pen.write(f"SCORE: {score}  HIGH SCORE: {high_score}", align="center", font=("Courier", 24, "bold"))

    time.sleep(0.1)
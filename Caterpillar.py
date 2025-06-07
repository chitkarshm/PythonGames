import random
import turtle as t
t.bgcolor('yellow')
caterpillar=t.Turtle()
caterpillar.shape('square')
caterpillar.color('red')
caterpillar.speed()
caterpillar.penup()
caterpillar.hideturtle()
food=t.Turtle()
food.shape('circle')
food.color('green')
food.penup()
food.hideturtle()
food.speed(0)
gamestarted=False
textturtle=t.Turtle()
textturtle.write('Press SPACE to start',align='center', font=('Arial', 16,'bold'))
textturtle.hideturtle()
scoreturtle=t.Turtle()
scoreturtle.hideturtle()
scoreturtle.speed(0)
def outsidewindow():
      leftwall=-t.window_width()/2
      rightwall=t.window_width()/2
      topwall=t.window_height()/2
      bottomwall=-t.window_height()/2
      t.penup()
      (x,y)=caterpillar.pos()
      print('position. x=', x, ', y=', y, 'leftwall=', leftwall, 'rightwall=', rightwall, 'topwall=', topwall, 'bottomwall=', bottomwall)
      outside=x < leftwall or x > rightwall or y < bottomwall or y > topwall
      return outside

def game_over():
      caterpillar.color('yellow')
      food.color('yellow')
      t.penup()
      t.hideturtle()
      t.write('GAME OVER!!', align='center', font=('Arial',30,'normal'))

def displayscore(currentscore):
      scoreturtle.clear()
      scoreturtle.penup()
      x=(t.window_width()/2)-50
      y=(t.window_height()/2)-50
      scoreturtle.setpos(x,y)
      scoreturtle.write(str(currentscore),align='right',font=('Arial',40,'bold'))

def placefood():
      food.ht()
      food.setx(random.randint(-200,200))
      food.sety(random.randint(-200,200))
      food.st()

def startgame():
      global gamestarted
      if gamestarted:
            return
      gamestarted=True

score=0
textturtle.clear()
caterpillarspeed=1
caterpillarlength=3
caterpillar.shapesize(1,caterpillarlength,1)
caterpillar.showturtle()
displayscore(score)
placefood()
while True:
      caterpillar.forward(caterpillarspeed)
      if caterpillar.distance(food) < 20:
            placefood()
            caterpillarlength=caterpillarlength+1
            caterpillar.shapesize(1,caterpillarlength,1)
            caterpillarspeed=caterpillarspeed+1
            score=score=10
            displayscore(score)
      if outsidewindow==True:
            game_over()
            break

def up():
      if caterpillar.heading()==0 or caterpillar.heading()==180:
            caterpillar.setheading(90)

def down():
      if caterpillar.heading()==0 or caterpillar.heading()==180:
            caterpillar.setheading(270)

def left():
      if caterpillar.heading()==90 or caterpillar.heading()==270:
            caterpillar.setheading(180)

def right():
      if caterpillar.heading()==90 or caterpillar.heading()==270:
            caterpillar.setheading(0)
t.onkey(startgame,'space')
t.onkey(up,'Up')
t.onkey(down,'Down')
t.onkey(left,'Left')
t.onkey(right,'Right')
t.listen()
t.mainloop()

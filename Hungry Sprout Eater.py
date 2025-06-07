from turtle import Turtle, Screen
from random import randrange
screen=Screen()
screen.bgcolor('red')
redraw=12
width,height=640,480
screen.setup(width,height)
vegsize=20
turtle=Turtle(shape='circle')
turtle.speed('slowest')
turtle.color('cyan')                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
turtle.penup()
turtlestamp=20

def turnright():
      screen.onkey(None,'Right')
      turtle.right(15)
      screen.onkey(turnright,'Right')
def turnleft():
      screen.onkey(None,'Left')
      turtle.left(15)
      screen.onkey(turnleft,'Left')
def good(food):
      x=randrange(vegsize-width//2,width//2-vegsize)
      y=randrange(vegsize-height//2,height//2-vegsize)

      food.goto(x,y)
      return ((x,y),food.stamp())
def eaten(food):
      global dot
      ((x,y))
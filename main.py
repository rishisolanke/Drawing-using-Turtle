import turtle
from shapes import *

# name your trutle
pen = turtle.Turtle()

# Set up your turtle

pen.speed(100)
pen.color(0,0,0)
wn = turtle.Screen()
wn.bgcolor(66,202,244)

# Start drawing

drawMountains(pen)
drawWall(pen,-150,-150,300,150,True)
drawDoor(pen,0,-150,60,80)
drawTower(pen,-150,-150,60,220, True)
drawTower(pen,90,-150,60,220,False)
drawFlag(pen,120,130,30,40,'#FFFF00')
drawLoophole(pen,-120,-120,10,30)
drawLoophole(pen,120,-120,10,30)
drawLoophole(pen,-120,0,10,30)
drawLoophole(pen,120,0,10,30)
drawLoophole(pen,-60,-80,10,30)
drawLoophole(pen,60,-80,10,30)

pen.hideturtle()

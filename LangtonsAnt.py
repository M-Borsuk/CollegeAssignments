# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 11:38:53 2020

@author: Matuesz
"""


import turtle as t
import numpy as np

screen = t.Screen()

screen.setup(width = 1.0, height = 1.0)

turtle = t.Turtle()
turtle.shape("square")
turtle.speed(0)
messenger = t.Turtle()
messenger.speed(0)
stamps = []
messenger.hideturtle()
messenger.penup()
messenger.setposition(-900, -450)
messenger.write("Steps: ",True,font=('monaco',30,'bold'),align='left')
for i in range(100000):
   messenger.setposition(-750, -450)
   messenger.write(i,True,font=('monaco',30,'bold'),align='left')
   messenger.undo()
   c=(np.round(turtle.xcor(),4),np.round(turtle.ycor(),4))
   if c in stamps:
       p = (np.round(turtle.xcor(),4),np.round(turtle.ycor(),4))
       turtle.color('white')
       turtle.stamp()
       stamps.remove(p)
       turtle.right(90)
       turtle.forward(15)
   else:
       p = (np.round(turtle.xcor(),4),np.round(turtle.ycor(),4))
       turtle.color('black')
       turtle.stamp()
       stamps.append(p)
       turtle.left(90)
       turtle.forward(15)
t.exitonclick()

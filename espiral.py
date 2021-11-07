# -*- coding: utf-8 -*-
"""
Cuadrado en espiral
"""
import turtle

turtle.clearscreen()
turtle.setpos(0,0)
i=1
lado=0
while i<=38:
    if i==1 or i%3==1:
        turtle.color('red')
    elif i==2 or i%3==2:
        turtle.color('blue')
    elif i==3 or i%3==0:
        turtle.color('green')
    turtle.forward(lado)
    turtle.left(90)
    i+=1
    lado+=10
    
turtle.hideturtle()
turtle.done()
try:
    turtle.bye()
except:
    pass
    
    

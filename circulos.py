# -*- coding: utf-8 -*-
"""
Círculo de círculos
"""
import turtle

turtle.clearscreen()
a=int(input('¿Cuántos círculos quieres?: '))
turtle.setpos(0,0)
for i in range(a):
    if i%2==0:
        turtle.color('red')
    else:
        turtle.color('blue')
    turtle.circle(100)
    turtle.left(360/a)
    i+=1

turtle.hideturtle()
turtle.done()
try:
    turtle.bye()
except:
    pass


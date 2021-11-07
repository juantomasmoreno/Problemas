# -*- coding: utf-8 -*-
"""
Círculo de estrellas
"""
import turtle
import math

def estrella(lado):
    for i in range(5):
        turtle.forward(lado)
        turtle.right(144)
        turtle.forward(lado)
        turtle.left(72)
        
def circulo(num, radio, lado):
    a=0
    for i in range(num):
        turtle.up()
        turtle.setpos(radio*math.cos(a),radio*math.sin(a))
        turtle.down()
        estrella(lado)
        a+=(2*math.pi/num)
        
def final():
    turtle.hideturtle()
    turtle.done()
    try:
        turtle.bye()
    except:
        pass
    
turtle.clearscreen()
turtle.speed(1000)
lado=10
for i in range(3):
    num=10+5*i
    radio=100*(i+1)
    circulo(num, radio, lado)
final()
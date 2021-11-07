# -*- coding: utf-8 -*-
"""
TRABAJO ACADÉMICO - Juan Tomás
[Las funciones punto() y posicion() están descritas pero no se utilizan]
"""
import turtle
import math

FUNCTIONS = (compile("x**2-1.5", "<string>", "eval"), 
             compile("math.cos(2*x)", "<string>", "eval"),
             compile("math.sin(2*x)", "<string>", "eval"),
             compile("math.sqrt(x+2)", "<string>", "eval"),
             compile("x**3-3*x", "<string>", "eval"),
             compile("0.5/x", "<string>", "eval"),
             compile("math.tan(0.55*x)", "<string>", "eval"),
             compile("1-x**2", "<string>", "eval"))

def f(n, x): 
    """
    Devuelve el valor de la función n para el valor x
    """
    try:
        return eval(FUNCTIONS[n - 1], {"x": x, "math": math})
    except ZeroDivisionError:
        x+=1/160
        
def inicio():
    """
    Comienza el programa
    """
    turtle.setup(640,640)
    turtle.speed(1000)
    
def ejeX():
    """
    Dibuja el eje X
    """
    turtle.up()
    turtle.setpos(-320,-320)
    turtle.down()
    x=-1.5
    for i in range(8):
        turtle.forward(80)
        turtle.left(90)
        turtle.forward(10)
        turtle.write(str(x))
        turtle.right(180)
        turtle.forward(10)
        turtle.left(90)
        x+=0.5
        
def ejeY():
    """
    Dibuja el eje Y
    """
    turtle.up()
    turtle.setpos(-320,-320)
    turtle.down()
    turtle.left(90)
    y=-1.5
    for i in range(8):
        turtle.forward(80)
        turtle.right(90)
        turtle.forward(10)
        turtle.write(str(y))
        turtle.right(180)
        turtle.forward(10)
        turtle.right(90)
        y+=0.5

def punto():
    """
    Convierte un punto de la gráfica a píxeles y lo dibuja
    """
    x=float(input('Introduce la coordenada X del punto: '))
    y=float(input('Introduce la coordenada Y del punto: '))
    posX=160*x
    posY=160*y
    turtle.up()
    turtle.setpos(posX,posY)
    turtle.down()
    turtle.dot()
    
def posicion():
    """
    Permite cambiar la posición de la tortuga
    """
    x=float(input('Introduce la coordenada X de la posición nueva: '))
    y=float(input('Introduce la coordenada Y de la posición nueva: '))
    posX=160*x
    posY=160*y
    turtle.up()
    turtle.setpos(posX,posY)
    
def lectura1():
    """
    Pregunta el número de la primera función
    """
    a=0.1
    while a!=round(a):
        a=turtle.numinput('TRABAJO ACADÉMICO - Juan Tomás',
                'Escribe el número de la primera función: ',
                minval=1, maxval=8)
        if a!=round(a):
            from tkinter import messagebox
            messagebox.showerror('ERROR', 'El valor no ha de tener decimales')
        elif a<0 or a>8:
            from tkinter import messagebox
            messagebox.showerror('ERROR', 'El valor debe estar entre 0 y 8')
    return a

def lectura2():
    """
    Pregunta el número de la segunda función
    """
    b=0.1
    while b!=round(b) or a==b:
        b=turtle.numinput('TRABAJO ACADÉMICO - Juan Tomás',
                'Escribe el número de la segunda función: ',
                minval=1, maxval=8)
        if a==b:
            from tkinter import messagebox
            messagebox.showerror('ERROR', 'Introduce un valor distinto')
        elif b!=round(b):
            from tkinter import messagebox
            messagebox.showerror('ERROR', 'El valor no ha de tener decimales')
        elif b<0 or b>8:
                from tkinter import messagebox
                messagebox.showerror('ERROR', 'El valor debe estar entre 0 y 8')
    return b

def dibujo(a,b): 
    """
    Dibuja las dos funciones solicitadas
    """
    x=-2
    y=0
    turtle.up()
    turtle.color('red')
    for i in range(640):
        y=f(a,x)
        turtle.setpos(160*x,160*y)
        turtle.down()
        x+=1/160
    x=-2
    y=0
    turtle.up()
    turtle.color('blue')
    for i in range(640):
        y=f(b,x)
        turtle.setpos(160*x,160*y)
        turtle.down()
        x+=1/160

def minimo():
    """
    Dibuja líneas verdes sobre el área entre el mínimo y el eje X
    """
    x=-2
    y=0
    turtle.up()
    turtle.color('green')
    for i in range(0,640,10):
        turtle.setpos(160*x,160*y)
        turtle.down()
        valorA=f(a,x)
        valorB=f(b,x)
        try:
            if valorA>valorB:
                turtle.setpos(160*x,160*valorB)
            else:
                turtle.setpos(160*x,160*valorA)
            x+=1/16
        except:
            x+=1/16
        turtle.up()

def final():
    """
    Finaliza el programa
    """
    turtle.hideturtle()
    turtle.done()
    try:
        turtle.bye()
    except:
        pass

inicio()
ejeX()
ejeY()
a=int(lectura1())
b=int(lectura2())
dibujo(a,b)
minimo()
final()

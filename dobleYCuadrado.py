# -*- coding: utf-8 -*-
"""
Calcula el doble y el cuadrado de un número
"""
import random

def dobleYCuadrado(x):
    return 2*x, x**2

x=int(input('Escribe un número cualquiera (o escribe 0 para un número aleatorio): '))
if x==0:
    x=random.randint(1,10000000)
tupla=dobleYCuadrado(x)
print(f'Tu número es {x}')
print(f'El doble de {x} es {tupla[0]}, y el cuadrado de {x} es {tupla[1]}')
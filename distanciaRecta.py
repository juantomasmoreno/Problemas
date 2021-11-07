# -*- coding: utf-8 -*-
"""
Calcula la distancia de un punto a una recta
"""

import math

x=float(input('Coordenada X del punto: '))
y=float(input('Coordenada Y del punto: '))
m=float(input('Pendiente de la recta: '))
b=float(input('Término independiente de la recta: '))

      
num=abs((m*x)-y+b)
den=math.sqrt((m**2)+1)
distancia=num/den

print(f'\n\nLa distancia entre el punto ({x},{y}) y la recta y = {m}x + {b} es...',distancia)
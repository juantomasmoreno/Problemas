# -*- coding: utf-8 -*"-
"""
Calcula la distancia entre dos puntos
"""

import math

x1=float(input('Coordenada X del primer punto: '))
y1=float(input('Coordenada Y del primer punto: '))
x2=float(input('Coordenada X del segundo punto: '))
y2=float(input('Coordenada Y del segundo punto: '))

distancia=math.sqrt((x2-x1)**2+(y2-y1)**2)
print('\n\nLa distancia entre ambos puntos es',distancia)
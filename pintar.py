# -*- coding: utf-8 -*-
"""
Función para pintar imágenes a través de la escala RGB
"""
from PIL import Image
from IPython.display import display

def pintar(foto, color, borde):
    (ancho, alto)=foto.size
    dic=foto.load()
    noColor=(color, borde)
    lista=[(ancho//2, alto//2)]
    while len(lista)>0:
        (x, y)=lista[-1]
        del lista[-1]
        if dic[(x, y)] not in noColor:
            dic[(x, y)]=color
            if dic[(x+1, y)] not in noColor:
                lista.append((x+1, y))  
            if dic[(x, y+1)] not in noColor:
                lista.append((x, y+1))
            if dic[(x-1, y)] not in noColor:
                lista.append((x-1, y))
            if dic[(x, y-1)] not in noColor:
                lista.append((x, y-1))

foto=Image.open('C:/Users/tomas/OneDrive - UPV/Escritorio/estrella.png')
pintar(foto, (0, 125, 250), (0, 0, 0))
display(foto)
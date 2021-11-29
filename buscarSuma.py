# -*- coding: utf-8 -*-
"""
Devuelve la posición de dos elementos en la lista que sumen "suma".
Si no es posible, devuelve "None".
"""

def buscarSuma(lista, suma):
    posiciones={}
    for i in range(len(lista)):
        elem1=lista[i]
        elem2=suma-elem1
        if elem2 in posiciones:
            return posiciones[elem2], i
        else:
            posiciones[elem1]=i
    return None

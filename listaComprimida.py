# -*- coding: utf-8 -*-
"""
Devuelve una lista con tuplas que muestran el valor y las veces que se repite
"""

def comprimir(m):
    res=[]
    tupla=(m[0], 1)
    for i in range(1,len(m)):
        elem=m[i]
        if tupla[0]==elem:
            tupla=(elem, tupla[1]+1)
        else:
            res.append(tupla)
            tupla=(elem, 1)
    res.append(tupla)
    return res

lista=[1, 1, 1, 3, 5, 2, 2, 6, 6, 6, 6, 4, 7, 7, 7, 7, 7, 7, 9]
lista_comprimida=comprimir(lista)
ejemplo=lista_comprimida[0]
print(lista_comprimida)
print(f'En este caso, {ejemplo[0]} se repite {ejemplo[1]} veces')
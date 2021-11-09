# -*- coding: utf-8 -*-
"""
Lista de números impares
"""
def eliminarPares(lista):
    a=0
    while a<len(lista):
        if lista[a]%2==0:
            del lista[a]
        else:
            a+=1
            
lista=[5, 2, 3, 4, 1, 7, 2, 78, 34, 12, 65, 43, 22, 22, 34, 76, 87, 97, 0, 6, 7, 4, 3, 13, 24]
eliminarPares(lista)
print(sorted(lista))
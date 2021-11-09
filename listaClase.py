# -*- coding: utf-8 -*-
"""
Borrar a alguien de la lista de clase
"""
lista_clase=['Juan', 'Adrián', 'Marisa', 'Fran', 'Paco', 'Julia', 'David', 'Marcos']
nombre=input('Escribe el nombre que quieres borrar: ')
try:
    indice=lista_clase.index(nombre)
    del lista_clase[indice]
    print(f'NUEVA LISTA: {lista_clase}')
except:
    print(f'{nombre} no está en la lista')
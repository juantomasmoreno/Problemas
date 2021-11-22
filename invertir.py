# -*- coding: utf-8 -*-
"""
Función para invertir un diccionario
"""
def invertir(dic):
    inv={}
    for key in dic:
        val=dic[key]
        if val not in inv:
            inv[val]=[key]
        else:
            inv[val].append(key)
    return inv

notas={'Pepe':5, 'Oscar':9, 'Juan':8, 'Ana':5}
print(invertir(notas))
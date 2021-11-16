# -*- coding: utf-8 -*-
"""
Buscar en la matriz y eliminar las filas y columnas que sumen lo mismo
"""
def sumaFila(m,fila):
    return sum(m[fila])
    
def sumaColumna(m,columna):
    a=0
    for i in range(len(m)):
        a+=m[i][columna]
    return a    
    
def buscar(m):
    numF=len(m)
    numC=len(m[0])
    for indiceF in range(numF):
        sumaF=(sumaFila(m,indiceF))
        for indiceC in range(numC):
            if sumaColumna(m,indiceC)==sumaF:
                return [indiceF,indiceC]
    return None

def borrarFila(m,fila):
    del m[fila]
    
def borrarColumna(m,columna):
    for i in m:
        del i[columna]

def mostrar(m):
    for fila in m:
        print(fila)
    
m=[[2, 8, 8, 0, 1, 4, 6],
   [4, 3, 1, 5, 6, 3, 2],
   [5, 9, 0, 1, 2, 3, 6],
   [9, 3, 5, 3, 4, 1, 1],
   [2, 2, 2, 4, 5, 6, 7],
   [1, 4, 2, 2, 4, 1, 7],
   [3, 8, 5, 4, 2, 9, 3]]

mostrar(m)
lista=buscar(m)
while lista!=None:
    fila=lista[0]
    columna=lista[1]
    print(f'\nLa fila {fila} y la columna {columna} suman {sumaFila(m,fila)}\n')
    borrarFila(m,fila)
    borrarColumna(m,columna)
    mostrar(m)
    lista=buscar(m)
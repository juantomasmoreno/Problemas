# -*- coding: utf-8 -*-
"""
Localizar valores en una matriz dispersa (el 80% de valores son 0)
"""
import random

def generar(f, c):
    '''
    Genera una matriz de f filas y c columnas
    '''
    matriz=[]
    for a in range(f):
        fila=[]
        for b in range(c):
            if random.randint(1,5)!=1:
                fila.append(0)
            else:
                fila.append(random.randint(-99,99))
        matriz.append(fila)
    return matriz

def mostrar(matriz):
    '''
    Muestra una matriz por pantalla
    '''
    for fila in matriz:
        c='|'
        for i in fila:
            c+=f'{i:4}'
        print (c+'|')
    
def convertir(matriz):
    '''
    Convierte matrices en diccionarios (f,c):valor
    '''
    dic={}
    numF=len(matriz)
    for a in range(numF):
        numC=len(matriz[a])
        for b in range(numC):
            elem=matriz[a][b]
            if elem!=0:
                dic[(a,b)]=elem
    return dic

m=generar(10,10)
mostrar(m)
print(f'\n{convertir(m)}')
        
        
    

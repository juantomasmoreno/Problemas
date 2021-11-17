# -*- coding: utf-8 -*-
"""
Plegado de un texto: Escribir una función que reciba un texto y una longitud.
La función devolverá una lista de cadenas de como máximo dicha longitud.
Las líneas deben cortarse en los espacios, sin cortar las palabras.
"""
def plegado(texto, longitud):
    '''
    Pliega el texto en líneas de longitud definida
    '''
    lista_lineas=[]
    lista_palabras=texto.split()
    if len(lista_palabras)>0:
        linea=lista_palabras[0]
        for i in range(1,len(lista_palabras)):
            palabra=lista_palabras[i]
            if len(linea)+len(palabra)+1<longitud:
                linea += ' ' + palabra
            else:
                lista_lineas.append(linea)
                linea=palabra
        return lista_lineas
            
def longitud():
    a=-1
    while a<=0:
        try:
            a=int(input('Escribe la longitud de las líneas: '))
        except:
            print('ERROR: introduce un número natural')
    return a

texto=input('Introduce aquí tu texto: ')
lista_texto=plegado(texto,longitud())
print('-'*10)
for linea in lista_texto:
    print(linea)
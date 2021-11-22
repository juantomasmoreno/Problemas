# -*- coding: utf-8 -*-
"""
Dado un texto, mostrar cuántas veces se repite cada palabra.
Después, mostrar las palabras que más se repiten.
"""
texto=input('Introduce el texto: ')
lista=texto.split()
dic={}
moda=[]
max=0
for PALABRA in lista:
    palabra=PALABRA.lower()
    if palabra not in dic:
        dic[palabra]=1
    else:
        dic[palabra]+=1
print('\nFRECUENCIA DE LAS PALABRAS')
for palabra in dic:
    print(f'{palabra} -> {dic[palabra]} veces')
    if dic[palabra]>max:
        max=dic[palabra]
        moda=[palabra]
    elif dic[palabra]==max:
        moda.append(palabra)
print('\nPALABRAS QUE MÁS SE REPITEN')
print(','.join(moda))
print(f'(Las palabras se repiten {max} veces)')

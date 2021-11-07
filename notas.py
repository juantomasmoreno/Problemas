# -*- coding: utf-8 -*-
"""
Estadísticas sobre notas
"""
def leerEntero(min, max, texto):
    x=min-1
    while x<min or x>max:
        try:
            x=int(input(texto))
            if x<min or x>max:
                print('ERROR: no está dentro del rango')
        except:
            print('ERROR: no es un número entero')
    return x

def leerReal(min, max, texto):
    x=min-1
    while x<min or x>max:
        try:
            x=float(input(texto))
            if x<min or x>max:
                print('ERROR: no está dentro del rango de notas')
        except:
            print('ERROR: no es un número real')
    return x

def fila(a, b, num):
    porcent=f'{100*b/num:.2f}%'
    print(f'{a:15}\u2502{b:^10}\u2502{porcent:^12}')
     
num=leerEntero(1, 1000, '¿Cuántas notas vas a introducir?: ')
suma=0
suspensos=0
aprobados=0
notables=0
sobres=0
matHonor=0
notaMax=0
notaMin=10
for i in range(num):
    nota=leerReal(0, 10, f'Escribe la {i+1}ª nota: ')
    suma+=nota
    if nota>notaMax:
        notaMax=nota
    if nota<notaMin:
        notaMin=nota
    if nota<5:
        suspensos+=1
    elif nota<7:
        aprobados+=1
    elif nota<9:
        notables+=1
    elif nota<10:
        sobres+=1
    else:
        matHonor+=1
print('\u2500'*40)
print(f'MEDIA = {suma/num:.2f}, MÍNIMA = {notaMin}, MÁXIMA = {notaMax}')
print('\u2500'*40)
print('RESUMEN DE CALIFICACIONES')
print('Calificación   '+'\u2502'+' Cantidad '+'\u2502'+' Porcentaje')
fila('SUSPENSO', suspensos, num)
fila('APROBADO', aprobados, num)
fila('NOTABLE', notables, num)
fila('SOBRESALIENTE', sobres, num)
fila('M. HONOR', matHonor, num)

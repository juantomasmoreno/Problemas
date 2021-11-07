# -*- coding: utf-8 -*-
"""
Piedra, papel o tijera
"""
import random
a=random.randint(1,3)
if a==1:
    j1='piedra'
elif a==2:
    j1='papel'
elif a==3:
    j1='tijera'
j2=input('¡Elige! (Escribe piedra, papel o tijera): ')
print('*'*20)
if j1==j2:
    print(f'¡Empate! Ambos habéis elegido {j1}')
elif ((j1=='piedra' and j2=='tijera') or
      (j1=='papel' and j2=='piedra') or
      (j1=='tijera' and j2=='papel')):
    print(f'¡Has perdido! El ordenador ha elegido {j1} y tú elegiste {j2}')
elif ((j2=='piedra' and j1=='tijera') or
      (j2=='papel' and j1=='piedra') or
      (j2=='tijera' and j1=='papel')):
    print(f'¡Has ganado! Has elegido {j2} y el ordenador eligió {j1}')
else:
    print('ERROR')
# -*- coding: utf-8 -*-
"""
Legibilidad de un texto
"""
f=int(input('Número de frases: '))
p=int(input('Número de palabras: '))
s=int(input('Número de sílabas: '))
print('*'*20)
ifsz = 206.835-(62.3*(s/p))-(p/f)
if ifsz>80:
    print(f'Texto muy fácil: IFSZ={ifsz:.2f}')
elif ifsz>=66:
    print(f'Texto bastante fácil: IFSZ={ifsz:.2f}')
elif ifsz>=56:
    print(f'Texto normal: IFSZ={ifsz:.2f}')
elif ifsz>=41:
    print(f'Texto algo difícil: IFSZ={ifsz:.2f}')
else:
    print(f'Texto muy difícil: IFSZ={ifsz:.2f}')


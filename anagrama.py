# -*- coding: utf-8 -*-
"""
Comprobación de si dos cadenas de texto son anagramas
"""
def es_anagrama(cadena1, cadena2):
    texto1=sorted(cadena1.lower().replace(' ',''))
    texto2=sorted(cadena2.lower().replace(' ',''))
    if texto1 == texto2:
        print(f'"{cadena1}" y "{cadena2}" son anagramas')
    else:
        print(f'"{cadena1}" y "{cadena2}" no son anagramas')

es_anagrama('Life on Mars', 'Alien forms')

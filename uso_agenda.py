# -*- coding: utf-8 -*-
"""
Usar una agenda
"""

from agenda import Agenda

ag = Agenda()
ag.nuevo_contacto('Ana', 123456789, 'ana@etsinf.es')

síes = ['Sí', 'SÍ', 'sí', 'Si', 'SI', 'si']
respuesta = 'Sí'
while respuesta in síes:
    ag.input_contacto()
    respuesta = input('\n¿Quieres introducir otro contacto? ')

print(ag)

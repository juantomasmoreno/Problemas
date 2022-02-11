# -*- coding: utf-8 -*-
"""
Compra de diversos objetos, y conversión de su precio a euros (si fuese necesario)
"""
def compra(divisas, file):
    res={}
    total=0
    with open(divisas) as divisas:
        for line in divisas:
            key,val=line.split()
            res[key]=float(val)
    with open(file) as f:
        for line in f:
            compra=line.split()
            if compra[-1] in res:
                producto=compra[:-2]
                precio=float(compra[-2])
                moneda=compra[-1]
            else:
                producto=compra[:-1]
                precio=float(compra[-1])
                moneda='EUR'
            producto=' '.join(producto)
            precio=precio*res[moneda]
            total+=precio
            print(f'{precio:8.2f} por {producto}')
    print('-'*50)
    print(f'PRECIO TOTAL: {total:8.2f} euros')
            
compra('divisas.txt','precios.txt')
        


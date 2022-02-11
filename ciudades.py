# -*- coding: utf-8 -*-
"""
Cruce de bases de datos de ciudades
"""
dic1 = {'Madrid': {'col1':11, 'col3':13}, 'Paris': {'col2':22, 'col4':24}}
dic2 = {'Madrid': {'col1':11, 'col2':12}, 'New York': {'col1':31, 'col4':34}}
dic3 = {'Paris': {'col1':21, 'col3':23}, 'Delhi': {'col1':41, 'col2':42}}
ldic=[dic1, dic2, dic3]
res={}

for d in ldic:
    for ciudad,datos in d.items():
        if ciudad not in res:
            res[ciudad]={}
        for col,val in datos.items():
            res[ciudad][col]=val
for línea in res.items():
    print(línea)
# -*- coding: utf-8 -*-
"""
Intersección y unión de dos conjuntos (sin usar & o |)
"""
def intersección(cA, cB):
    res=set()
    if len(cA)>len(cB):
        cA,cB = cB,cA
    for i in cA:
        if i in cB:
            res.add(i)
    return res

def unión(cA,cB):
    res=cA.copy()
    for i in cB:
        res.add(i)
    return res
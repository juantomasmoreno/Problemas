# -*- coding: utf-8 -*-
a={'llaves':2, 'puerta':4, 'ventana':10, 'televisión':2}
b={'llaves':1, 'perro':1, 'peces':4, 'puerta':2, 'ventana':3}
res={}
objetos=set.union(set(a),set(b))
for key in objetos:
    res[key]=a.get(key,1)+b.get(key,1)
print(res)

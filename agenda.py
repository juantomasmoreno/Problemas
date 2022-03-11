# -*- coding: utf-8 -*-
"""
Crear una agenda
"""

class Contacto:
    def __init__(self, nom, tel, em):
        self.nombre = nom
        self.telefono = tel
        self.email = em
        
    def __str__(self):
        return 'Nombre: {}\nTeléfono: {}\nEmail: {}\n'.format(self.nombre, self.telefono, self.email)
    
class Agenda:
    def __init__(self):
        self._contactos = {}
    
    def nuevo_contacto(self, nom, tel, em):
        if nom in self._contactos.keys():
            return False
        else:
            nuevo = Contacto(nom, tel, em)
            self._contactos[nom] = nuevo
            return True
        
    def input_contacto(self):
        a = input('Introduce el nombre del contacto: ')
        b = int(input('Introduce el número de teléfono: '))
        c = input('Introduce el correo electrónico: ')
        self.nuevo_contacto(a, b, c)
        
    def buscar_contactos(self, texto):
        res = []
        for c in self._contactos.keys():
            if texto in c:
                res.append(c)
        return res
    
    def modificar_telefono(self, nom, tel):
        if nom in self._contactos.keys():
            self._contactos[nom].telefono = tel
            return True
        else:
            return False
        
    def borrar_contacto(self, nom):
        if nom in self._contactos.keys():
            del self._contactos[nom]
            return True
        else:
            return False
        
    def __len__(self):
        res = len(self._contactos)
        return res
    
    def __str__(self):
        res = '\n CONTACTOS:\n'
        for c in self._contactos.values():
            res += f'\n{str(c)}'
        return res
            

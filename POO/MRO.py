# MRO -> Method Resolution Order
from Personaje import Personaje

class Villano(Personaje):
    def __init__(self, nombre, defecto='Codicioso'):
        super().__init__(nombre)
        self.defecto = defecto
    def destruirMundo(self):
        print('Acabando con el mundo')

class SuperHeroe(Personaje):
    def __init__(self, nombre,virtud='Bueno'):
        super().__init__(nombre)
        self.virtud = virtud    
    def hacerElBien(self):
        print('Salavando al mundo')

class PersonajeNeutral(Villano, SuperHeroe):
    def __init__(self, nombre, defecto, virtud):
        Villano.__init__(self, nombre, defecto)
        SuperHeroe.__init__(self, nombre, virtud)
    def decirDialogo(self):
        print('Estoy diciendo algo')

neutral = PersonajeNeutral('Anderson','malo','respetuoso')
print(PersonajeNeutral.mro())

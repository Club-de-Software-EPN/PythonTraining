# Herencia

class Personaje:
    def __init__(self, nombre):
        self.nombre = nombre
    def registrado(self):
        print('Personaje registrado!!!')

class SuperHeroe(Personaje):
    def __init__(self, nombre, virtud='Bondadoso'):
        super().__init__(nombre)
        self.virtud = virtud
    def salvarMundo(self):
        print('Estoy salvando al mundo')

personaje = Personaje('Persona random')
personaje.registrado()
superheroe = SuperHeroe('Spiderman','Honesto')
superheroe.registrado()
superheroe.salvarMundo()
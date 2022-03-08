# Herencia

class Personaje:
    def __init__(self, nombre):
        self.nombre = nombre
    def registrado(self):
        print('Personaje registrado!!!')

class SuperHeroe(Personaje):
    #def __init__(self, nombre, virtud='Bondadoso'):
        #super().__init__(nombre)
        #self.virtud = virtud
    def __init__(self, nombre,virtud='Bondadoso'):
        super().__init__(nombre)
        self.virtud = virtud

    def registrado(self):
        print('Superhéroe registrado!!')

    def salvarMundo(self):
        print('Estoy salvando al mundo')

    def pelear(self):
        print('Peleando por la justicia!')

class Villano(Personaje):
    def __init__(self, nombre, defecto='Ambicioso'):
        super().__init__(nombre)
        self.defecto = defecto
    def pelear(self):
        print('Peleando por destruir el mundo!')

personaje = Personaje('Persona random')
personaje.registrado()
superheroe = SuperHeroe('Spiderman','Honesto')
superheroe.registrado()
superheroe.salvarMundo()
superheroe.pelear()
villano = Villano('Guason')
villano.pelear()
# Polimorfismo
# Adecuar los compartemientos en cada una de las clase

class Personaje:
    def __init__(self, nombre):
        self.nombre = nombre
    def saludar(self):
        print('Holaa!!!')

class SuperHeroe(Personaje):
    def __init__(self, nombre,virtud='Bueno'):
        super().__init__(nombre)
        self.virtud = virtud    
    def saludar(self):
        print('Salavando al mundo')

class Villano(Personaje):
    def __init__(self, nombre, defecto='Codicioso'):
        super().__init__(nombre)
        self.defecto = defecto
    def saludar(self):
        print('Acabando con el mundo')

superheroe = SuperHeroe(nombre='Batman')
villano = Villano(nombre='Guason')

superheroe.saludar()
villano.saludar()



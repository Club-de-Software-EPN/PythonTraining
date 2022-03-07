# Clases con métodos y atributos

# Método init (contructor)
# Siempre se va ejecutar y es lo primero en ejecutarse

class Personaje:
    # Atributos
    def __init__(self, nombre, tipo, edad):
        self.nombrePersonaje = nombre
        self.tipo = tipo        
        self.edad = edad
    # Métodos especiales get y set
    def getNombrePersonaje(self):
        return self.nombrePersonaje
    def setNombrePersonaje(self, nuevoNombre: str):
        self.nombrePersonaje = nuevoNombre
    # Métodos
    def saludar(self):
        print(f'Hola, soy un personaje\nMi nombre es {self.nombrePersonaje} y soy un {self.tipo}')
    

personaje1 = Personaje('Batman','Héroe',35)
personaje2 = Personaje('Spiderman','Héroe',23)

personaje1.saludar()
personaje1.saludar()


print('Nombre antes del set ',personaje2.getNombrePersonaje())
personaje2.setNombrePersonaje('Venom')
print('Nombre después del set ',personaje2.getNombrePersonaje())
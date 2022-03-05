# Clases con métodos y atributos

# Método init (contructor)
# Siempre se va ejecutar y es lo primero en ejecutarse

class Personaje:
    # Atributos
    def __init__(self, nombre, tipo, edad):
        self.nombrePersonaje = nombre
        self.tipo = tipo
        self.edad = edad
    
    # Métodos

personaje1 = Personaje('Batman','Héroe',35)
personaje2 = Personaje('Spiderman','Héroe',23)

print(personaje1.nombrePersonaje)
print(personaje1.tipo)
print(personaje2.nombrePersonaje)
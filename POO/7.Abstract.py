from abc import ABC, abstractmethod

# Interfaces -> solo tien métodos, ya no especifique la implementación de los métodos
# Métodos que aún no son implementados son conocidos conocidos abstractos
# Para poder tenr una interfaz necesariamente se neceista al menos un método abstracto

class Animal(ABC):
    @abstractmethod
    def darInformacion(self):
        pass

# Herencia -> Métodos 
class Mamifero(Animal):
    def saludar(self):
        print('Hola')
    def darInformacion(self):
        print('Me alimento de leche')

class Reptil(Animal):
    def darInformacion(self):
        print('Soy de sangre fría')

mamifero = Mamifero()
mamifero.darInformacion()

reptil = Reptil()
reptil.darInformacion()
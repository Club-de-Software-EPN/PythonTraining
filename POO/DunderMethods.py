# Métodos Dunder Python

class Personaje:
    # init -> incializar atributos
    def __init__(self, nombre='Juan'):
        self.nombre = nombre
        self.cualidades = ['Bueno','Bondadoso','Sincero']
    def saludar(self):
        print('Holaa!!!')
    # to string
    def __str__(self) -> str:
        return f'Clase Personaje, el nombre es {self.nombre}'
    def __len__(self) -> str:
        return 1
    def __getitem__(self, i):
        return self.cualidades[i]
    def __call__(self):
        return f'Si para que me buscas?'

personaje = Personaje()
print(personaje.__str__())
print(personaje.__len__())
print(personaje.__getitem__(1))
print(personaje.__call__())
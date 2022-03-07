# Métodos de clase y métodos estáticos
# Método clase: Son aquellos que requieren tener una instancia
# Método estático: Son aquellos métodos que no requieren una instancia de la clase
class Carro:
    def __init__(self, placa='ABC-123', color='rojo'):
        self.placa = placa,
        self.color = color

    # Métdo clase
    def rodar(self):
        print(f'Soy el auto de placas {self.placa} y soy de color {self.color}')

    # Otra forma de definir métodos de la clase
    @classmethod
    def velocimetro2(cls, velocidad):
        print(f'Velocidad actual: {velocidad}')
    
    @staticmethod
    def velocimetro(velocidad: str):
        print(f'Velocidad actual: {velocidad}')


#carro1 = Carro()
#carro2 = Carro(placa='BDC-567', color='azul')

#carro1.rodar()

Carro.velocimetro('20 km/h')

carro1 = Carro()
carro1.velocimetro2('50 km/h')



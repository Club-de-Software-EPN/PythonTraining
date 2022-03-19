# Posición para cualqueir elementos gráfica

class Posicion:
    def __init__(self, posiciones: tuple) -> None:
        self.x, self.y = posiciones

    def setX(self, valorX):
        self.x = valorX

    def setY(self, valorY):
        self.y = valorY

    def obtenerCoordenadas(self):
        return self.x, self.y

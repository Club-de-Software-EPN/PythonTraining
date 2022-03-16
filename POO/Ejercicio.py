# Resolución ejercicio

class Multa:
    def __init__(self, nombreMulta, tipo) -> None:
        self.nombreMulta = nombreMulta
        self.tipo = tipo
        self.valor = 0
    def multar(self):
        if self.tipo == 'Leve':
            self.valor = 100
        elif self.tipo == 'Grave':
            self.valor = 300    


class Registro:
    def __init__(self, nombre, matricula):
        self.nombre = nombre
        self._matricula = matricula
        self.listaMultas = []

    def registar(self, multa: Multa):
        self.listaMultas.append(multa)

    def getMatricula(self):
        return self._matricula

    def setNombre(self, nuevoNombre: str):
        if nuevoNombre != self.nombre:
            self.nombre = nuevoNombre
        else:
            print('No se puede actualizar con el mismo nombre')
    
    def __str__(self) -> str:
        return f'El ciudadano: {self.nombre} con matricula {self._matricula} tiene las {len(self.listaMultas)} multas '

    
registroAnderson = Registro('Anderson','ABC-123')
print(registroAnderson.__str__())

multa1 = Multa('Exceso velocidad','Grave')
registroAnderson.registar(multa1)
print(registroAnderson.__str__())

multa2 = Multa('Muy baja velocidad','Leve')
registroAnderson.registar(multa2)
print(registroAnderson.__str__())


print(registroAnderson._matricula)
print(registroAnderson.getMatricula())


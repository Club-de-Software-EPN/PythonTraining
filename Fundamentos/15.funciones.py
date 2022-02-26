# Funciones -> def
# A (regla de correspondencia) -> B
# a -> f -> b

# Procedimiento  (función vacia)
def saludar():
    print('Hola!!!')

saludar()

edades = [18,5,20,22,17,14.5,2]

# Funciones
# 1. Recibir parámetros
def esMayorEdad(edad: int):
    if edad >= 18:
        return True
    return False

for edad in edades:
    print(esMayorEdad(edad))

# 2. Recibir varios parámtros
def saludar2(nombre: str, apellido):
    return f'Saludos {nombre} {apellido}'

print(saludar2('Anderson','Cárdenas'))

# 3. Parámetros por defecto
def saludar3(nombre='Hector', apellido='Zambrano'):
    return f'Saludos {nombre} {apellido}'

print(saludar3())
print(saludar3('Fernando'))
print(saludar3(apellido='Real'))
print(saludar3('Fernando','Real'))

# 4. Llamar a una función dentro de otra 
def saludar4():
    print('Hola a todos!!!')
    print(saludar3())

saludar4()

# Documentación de funciones

def calcularCubo(numero: int):
    '''
    Permite calcular el cubo de un número
    numero: Número entero
    return: El cubo de la entrada
    '''
    return numero**3

print(calcularCubo(3))
print(calcularCubo.__doc__)

# Funciones args
# *args
# argumentos
# Número indefinido de valores
def listarAlumnos(*alumnos):
    print(f'Alumno: {alumnos}')

listarAlumnos('Anderson')
listarAlumnos('Anderson','Andrés','Bryan','Janeth','Jeremy')

def listarAlumnos2(*alumnos):
    for alumno in alumnos:
        print(f'Alumno: {alumno}')

listarAlumnos2('Anderson')
listarAlumnos2('Anderson','Andrés','Bryan','Janeth','Jeremy')

# **kwargs
# key word args
# Número indefinido de variables de diferente tipo
def listarAlumnos3(**alumnos):
    print('La edad es: ', alumnos['edad'])

listarAlumnos3(nombre='Anderson',apellido='Cárdenas',edad=22)


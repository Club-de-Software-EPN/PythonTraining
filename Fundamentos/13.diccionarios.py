# Diccionarios  -> dict()
# Hash maps
# Tiene dos partes: clave(llave) y el valor
# Tras la inicialización la clave es inmutable
# Clave puede ser de cualquier tipo de dato al igual que el valor
# No soporta la indexación
# CRUD -< Create, update, read, delete

diccionario1 = {
    'i1': 1,
    'i2': [True, 'Anderson',6]
}

print(type(diccionario1))
print(diccionario1)

# Acceder a los datos de un diccionario
print(diccionario1['i2'])

materias = {
    'audiotoriaInformatica': 8,
    'webAvanzada2': 10
}
edad = 22
llaveVariable = 'cedula'
persona = {
    'nombre': 'Anderson',
    'apellido': 'Cárdenas',
    'edad': edad,
    'casado': False,
    21: True,    
    llaveVariable: '1726744814',
    'materias': materias
}

print(type(persona['nombre']))
print(persona['edad'])
print(persona['casado'])
print(persona[21])
print(persona[llaveVariable])
print(persona['materias'])


listaPrueba = [0,1,2,3,4]

print('Métodos')
# obtener un valor
print(persona.get('edad'))
# actualizar un dato
print(persona.update({'edad':23}))
# agregar valor a un diccionario ya creado
persona['universidad'] = 'EPN'
print(persona)
#eliminar valores de un diccionario
# pop eliminar a través de la llave
persona.pop(21)
print(persona)
# eliminación del valor 

# 1. Saber cuales son solo los valores del diccionario
print(persona.values())
# 2. Saber cuales son solo las llaver del diccionario
print(persona.keys())
# 3. Diccionario mapeado
print(persona.items())
# 
def obtenerLlave(valorBuscar):
    for llave, valor in persona.items():
        if valorBuscar == valor:
            return llave
        #return Exception

print('Llave encontrada:',obtenerLlave('1726744814'))
persona.pop(obtenerLlave('1726744814'))
print(persona)

# pop item -> eliminar el último valor insertado en el diccionario (3.7)
persona.popitem()
print(persona)

# ¿Qué pasatía si pido obtener un valor ?
print(persona.get('mascota', 'No existe este valor'))

copiaPersona = persona.copy()
print(copiaPersona)

# Numerable
print(len(copiaPersona))

# 
#for i in listaPrueba:
    #str(i): 

#diccionario10 = {'valor1':1,'valor2':2}

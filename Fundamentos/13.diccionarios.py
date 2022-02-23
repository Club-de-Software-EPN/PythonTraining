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

# Eliminar todo
copiaPersona.clear()
print(copiaPersona)

# COnversión entre lista y diccionario
# 1
listaPrueba = [0,1,2,3,4]
diccionarioPrueba = {}
for i in listaPrueba:
    diccionarioPrueba[i] = i

print(diccionarioPrueba)

# 2
diccionarioPrueba2 = {}
listaLlave = ['n0','n1','n2','n3','n4']
listaPrueba2 = [0,1,2,3,4]
for i in range(len(listaLlave)):
    diccionarioPrueba2[listaLlave[i]] = listaPrueba2[i]
print(diccionarioPrueba2)

# 3
diccionarioPrueba3 = dict(zip(listaLlave,listaPrueba2))
print(diccionarioPrueba3)

#diccionario10 = {'valor1':1,'valor2':2}

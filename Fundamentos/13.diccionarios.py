# Diccionarios  -> dict()
# Hash maps
# Tiene dos partes: clave(llave) y el valor
# Tras la inicialización la clave es inmutable
# Clave puede ser de cualquier tipo de dato al igual que el valor
# No soporta la indexación

from sklearn.metrics import precision_score


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
print(persona)

# 
#for i in listaPrueba:
    #str(i): 

#diccionario10 = {'valor1':1,'valor2':2}

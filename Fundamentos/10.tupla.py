# Tupla -> tuple
# Inmutable 

from sqlalchemy import tuple_


tupla1 = (3,4,5,6,6)
print(tupla1)
print(type(tupla1))

#Accediendo a los elemntos de la tupla
print(tupla1[0])

# Tupla con diferentes tipos de datos
tupla2 = (True,25,'Hola')
print(tupla2)

# Avergiuar si un elemento se encuentra o no en una lista
print(False in tupla2)
print('python' in tupla2)
print(25 in tupla2)
print(100 not in tupla2)

# Métodos de la tupla
print(tupla1.index(3))
# print(tupla1.index(100)) en caso de no estar incluido devuelve un error
print('Tamaño de una tupla', len(tupla1))
print('¿cuantos numeros 6 estan en la tupla 1?',tupla1.count(6))

# Descomprensión
dimensiones = (500,600)
dimensionX, dimensionY = dimensiones
print(dimensionX)
print(dimensionY)


# COnvertir de una lista hacia tupla
lista1 = [85,26,98]
miTupla = tuple(lista1)
print(miTupla)

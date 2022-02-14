# Listas list()
# Inicialización []
# Listas no tiene un espacio definido

lista1 = [1,2,3,4,5,6,7,8,9,10]
print(type(lista1))

# Listas combinadas
lista2 = ['a','b','c',85, 74, True, 35.68]
print(lista2)

# Métodos y las operaciones de las listas

# Indexación
# averiguar largo o númeri de elemento que tiene una lista
print(len(lista2))
# Accediendo a los elementos de la lista
print(lista2[0])
print(lista2[6])

#Cambiar los valores de la lista
lista2[5] = False
print(lista2)

#Indexación entre intervalos
print(lista2[1:3])
print(lista2[::-1])

#lista alumnos
listaAlumnos = ['Anderson','Andrés','Cristo','Janeth','Mario']
# obteenr una nueva lista con las dos últimas personas
listaAlumnos2 = listaAlumnos[1:]
print(listaAlumnos2)
print(type(listaAlumnos2))

# agrega datos al final de una lista
listaAlumnos2.append('Fernanda')
print(listaAlumnos2)

# agrega en una posición en específico
# Indicamos el índice en el que vamos a insertar y el valor
listaAlumnos2.insert(3,'Bryan') 
print(listaAlumnos2)

#como agregar al final otra lista
listaAlumnos2.extend(['Pablo','Jose'])
print(listaAlumnos2)

# Retirar elementos
# pop recibe el índice que quiero retirar
# Pero si no le paso el índice retirará el último elemento
listaAlumnos2.pop()
print(listaAlumnos2)

#remover con un índice en específico
listaAlumnos2.pop(1)
print(listaAlumnos2)

#retiramos un valor en específico de la lista
listaAlumnos2.remove('Pablo')
print(listaAlumnos2)

#¿Qué pasa si hay dos elementos con el mismo nombre?
listaAlumnos2.extend(['Alejandro','Alejandro'])
print(listaAlumnos2)
listaAlumnos2.remove('Alejandro')
print(listaAlumnos2)

# Operador 
print('Andrés' in listaAlumnos2)
print('Samatha' in listaAlumnos2)

# Hacer una copia
copialistaAlumnos = listaAlumnos2[::]
print(copialistaAlumnos)
copialistaAlumnos2 = listaAlumnos2.copy()
print(copialistaAlumnos2)

#Invertir la copia
print(copialistaAlumnos[::-1])
copialistaAlumnos2.reverse()
print(copialistaAlumnos2)

# Encontrar índice de un elemento
print(copialistaAlumnos)
print(copialistaAlumnos.index('Janeth'))

#¿Que pasaría si solicito un índice de un elemento que no se encuentra en la lista?
#print(copialistaAlumnos.index(58))
#Producirá un erro si el elemnto no se encuentra enlistado

# Ordenar
copialistaAlumnos.sort()
print(copialistaAlumnos)

lista4 = [85,47,68,25]
lista4.sort(reverse=True)
print(lista4)

# Ordenar una lista con diferentes tipos de datos no es posible
#lista5 = ['A',58,68]
#lista5.sort()
#print(lista5)

# Pueden convertir un string a lista
cadenaTexto = 'Las universidades piensan en retornar a la presencialidad'
listadeTexto = list(cadenaTexto)
#print(listadeTexto)

# Separar en palabras 
listaPalabra = cadenaTexto.split(' ')
print(listaPalabra)

#contar el número de veces que una palbra esta en la lista
print(listaPalabra.count('universidades'))

# join
saludo = 'Saludo: '
oracion = saludo.join([' buenos días','buenas tardes'])
print(oracion)

lista5 = ['Hola']
lista6 = ['cómo estás?']
print(type(lista6))
lista5.extend(lista6)
temp = lista5.copy()
print(lista5)
print(temp)

# Declarar una lista vacía
lista7 = []

# elimianr todos los elemntos de la lista
temp.clear()
print(temp)


# Unpacking, desempaquetado de una lista
print(listaAlumnos)
nombre1, nombre2 = listaAlumnos[0:2]
print(nombre1)
print(nombre2)

nombre1, nombre2, *nombres = listaAlumnos
print(nombre1)
print(nombre2)
print(nombres)

nombre1, nombre2, *nombres, nombre3 = listaAlumnos
print(nombre1)
print(nombre2)
print(nombres)
print(nombre3)


# Lista de listas
matriz = [
    [0,1,0],
    [1,1,1],
    [0,0,2]
]
print(matriz)
print(matriz[2][2])
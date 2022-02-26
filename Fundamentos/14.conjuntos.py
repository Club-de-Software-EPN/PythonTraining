# Conjuntos -> set
# Sets 
conjunto1 = {1,2,3,4}
print(conjunto1)
print(type(conjunto1))

conjunto2 = {1,2,3,4,4}
print(conjunto2)

# Crear una lista con elemntos únicos
listaEjemplo = [14,15,16,63,63,63,89,75,14,15]
conjunto3 = list(set(listaEjemplo))
print(conjunto3)

# ¿Es posible crear conjuntos no numéricos?
conjunto4 = {'Andrés','Bryan','Cristo', 'Andrés'}
print(conjunto4)

# ¿Es posible crear conjuntos de diferentes tipos de datos?
conjunto5 = {78, 59235.2, True, False, 'Anderson'}
print(conjunto5)

# Métodos de los conjuntos
cA = {1,2,3,4,5,6,7}
cB = {3,4,5,11}

# Agregar un elemento al conjunto
cA.add(8)
print(cA)

cA.add(1)
print(cA)

# Averiguar el tamaño de un conjunto (cardinalidad)
print(len(cA))

# Eliminar un elemnto del conjunto
cA.discard(8)
print(cA)

#Update conjunto
cA.update({6,7,8,9})
print(cA)

# Copiar un conjunto
cD = cA.copy()
print(cD)

# pop,  elimina el primer elemento
cD.pop()
print(cD)

# limpiar
cD.clear()
print(cD)

# Métodos entre dos conjuntos
print('Conjunto A: ',cA)
print('Conjunto B: ',cB)
# Diferencia
print('Diferencia: ',cA.difference(cB))
# Unión
cC = {10}
print('Unión: ',cA.union(cC))
# Intersección
print('Intersección: ',cA.intersection(cB))
# Diferencia simétrica
# A ^ B = (A-B)U(B-A)

print('Diferencia Simétrica: ',cA.symmetric_difference(cB))

# SI dos conjuntos son disjuntos
print(cA.isdisjoint(cB))
cE = {100,20,23}
print(cA.isdisjoint(cE))

# Averiguar si es subconjunto
print(cB.issubset(cA))
# Averiguar si es superconjunto
print(cA.issuperset(cB))
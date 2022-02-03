# Asignación, es darle un valor a ese espacio 
# = 
x = 5
print('El valor de la variable x es: ',x)

# Asingación sin valor
# None = no tiene ningún tipo de dato
variable1 = None
print(type(variable1))
print('el valor de la variable 1 es: ', variable1)

# Inicializar un variable y con el valor de 10
y = 10  # En este punto la variable tiene el valor de 10
print(y)
# Multiplicar por dos
y = y * 2  # 10 *2 = 20. En este punto la variable y tiene asignado 20
print(y) # 20
# Multiplicar por dos
print(y*2)  #40        
print(y)    #20

## Asignación con diferentes tipos
y = 'Saludo'
print(y)

# Multiples asignaciones
# Crear las variables a y b con los varoles de 2 y 3
a = 2
b = 3

a, b, c, saludo = 2, 3, 5, 'Hola'
print(a+b+c)
print(saludo)

# Asignación del valor de una variabla a otra variable
# se copia el contenido en ese instante
saludo2 = saludo
print(saludo2)
saludo = 'Buenas tardes'
print(saludo2)

# Ejercicio
x1 = 4 
y1 = x1 + 1
x1 = 2
print('x1 = ',x1,' y ',' y1 = ',y1)  #x1=2    #y1=5

# Ejercicio 2
# errores en la asignación
x2, y2 = 10, 11
z2  = x2 # z2 = 10
y2 =  z2 + 2
print(x2,', ',y2,', ',z2)

# APuntar a nulo
#
#  hex -> variables
#x2, y2 = z3 +1 , 5 # error 
# 
#x5, x2 = x5+1, 2  # no es un error



# Enteros -> int
# Conversiones de datos

# Importación
import math

num1 = input('Ingresa un número')  #num es tipo str
print(type(num1))
num1 = int(num1) # Conversión de a entero
print(num1+20)

# En una sola línea de código, tomo la entrada de input y la convierto a entero
num2 = int(input('Ingrese otro número: '))
print(num2+2)

# 
#num3 = int(True)
# True -> 1
# Falso -> 0
#print(num3)

# Operadores numéricos
a,b = 2,3

# Suma
print('\n\tOperaciones con números\n')
print('Suma: ',a+b)
# Resta
print('Resta: ',a-b)
# Multiplicación
print('Multiplicación: ',a*b)
#División
print('División: ',a/b)
# División de dos números siempre será un número flotante
#print(int(10/3))

# Módulo
print('Módulo; ',10%2)

# División entera
print('Divisón entera: ', 10//3)

# Potencia
print('Potencia: ',2**3)

# Raíz
print('Raíz con potencia: ',64**(1/2))
print('Raíz cuadrada: ', math.sqrt(64))

# -------------------------------------
# Floats  -> float,  consideraciones separación con el .
# -----------------------------------
numeroFlotante = float(input('Ingresa un  número decimal:'))
print(numeroFlotante)

# Operadores son los mismos que los enteros

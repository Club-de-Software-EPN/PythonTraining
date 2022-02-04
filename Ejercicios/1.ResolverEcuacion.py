# Programa que permita resolver de segundo grado
# ax^{2}+bx+c=0 // a, b y c son números enteros
# Pedir al usuario que ingrese los valores de a, b y c
# Imprimeros en consola la ecuación de segundo grados
# Mostrar las dos soluciones x1, x2
import math
print('\tRaices de ecuaciones de segundo grado')
print('Polinomio de la forma: ax^2+bx+c')
a = int(input('Ingresa a: '))
b = int(input('Ingresa b: '))
c = int(input('Ingresa c: '))
# Calcular las soluciones
x1 = (-b + math.sqrt((b**2)-(4*a*c)) ) / (2*a)
x2 = (-b - math.sqrt((b**2)-(4*a*c)) ) / (2*a)
print('La ecuación ',a,'x^2 +',b,'x +',c, 'tiene las soluciones: ')
print('x1=',x1)
print('x2=',x2)

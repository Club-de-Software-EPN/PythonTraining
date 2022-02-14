## Booleanos -> bool()
# Dos tipos
# False y True

# True -> 1
# False -> 0

variable1 = True
variable2 = False

print(type(variable1))

print(variable1.bit_length())

## Operadores
# Asignación =
# Aritméticos
# Strings + -> concatenación
#Asignación Complementarios
x = 4
x += 5 #le sumo 5
print(x)
x **= 2
print(x)

# Operadores Lógicos
# Conjunción -> and
print(variable1 and variable2)
print(True and True)
print(False and False)

#Disyunción -> or
print('OR')
print(variable1 or variable2)
print(False or False)

#Negación -> not
print(not variable1)
print(not variable2)

# Ejemplo
print('2: ',True and True) # True and True 2. Operación lógica de toda la expresión



# Operadores bit a bit
# AND
print(True & True) # 1 & 1 3. Tomar el truly or falsy y hacer la operación and
# OR
print(4 | False) 
#Operador xor
print(4 ^ 5) # 1 ^ 1 1. convertir a binario y de ahí hacer la operación
# Not
print(~False)
# Desplazamiento de bit a bit hacia la derecha
print(True >> False)
# Desplazamiento bit a bit hacia la izquierda
print(True << False)

# Operadores Bit a bit
# Base 10 -> 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 
# Binario > 0, 1 
# 1 Byte -> 8 bits

# 10101010 -> 1 byte
# 2^{7}       2^{3},2^{2},2^{1},2^{0}
#              16,4,2,1

# Computadora representame el número tres en un byte
#   0000011  -> 3 (base 10)
#Computadora representame el número 5 en un byte
#                 5 (base 10)   4 +1 =5
#  00000101  -> 5 (base 10)


#   101
# & 000
#   ---
#   000

#   1101
# & 1001
#   ----
#   1001

# Ejemplo de los operadores bit a bit
var1 = 2  # 1 0  
var2 = 3  #  1 1
var3 = 5 # 1 0 1

print('Probando los binarios')
print(var1 & var2)
# var1 ->  1 0
# var2 ->& 1 1
#        ------
#          1 0  -> 2
#         2^{1}=2 2^0=1
# base 10
print(var1 | var2)
# var1 ->  1 0
# var2 ->| 1 1
#          ----
#           11 -> 3 (base 10) 
print(var1 ^ var2)
# var1 ->  1 0
# var2 ->^ 1 1
#          ----
#          01 -> 1 (base10)
print(~var1)
# va1 ->~00000010
#        11111101
print(var1>>var2)
#   10
#   11  
#    0
print(var1<<var2)
print(True&True)
#      1  &  1
#      1 -> True

# Operadores de Pertenencia
# Identidad
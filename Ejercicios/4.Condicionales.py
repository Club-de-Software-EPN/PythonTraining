# Capicuas
# Palindromos

# Solcitar al usuario que ingrese por teclado un texto le vamos a indicar si lo ingresa es o 
# no un palíndromo

print('\tIdentificador de palíndromos')
texto = str(input('Ingrese una cadena de texto: '))
print('\nPalabra de izquierda a derecha: '+texto)
print('Palabra de derecha a izquierda: '+texto[::-1]+'\n')
if texto == texto[::-1]:
    print('Ingresaste un palíndromo!!!')
elif texto.lower() == texto[::-1].lower():
    print('Palíndromo, ignrnado las mayúsculas')
elif texto.replace(' ','') == texto[::-1].replace(' ',''):
    print('Palíndromo ignorando los espacios')
elif texto.lower().replace(' ','') == texto[::-1].lower().replace(' ',''):
    print('Palíndromo ignorando las mayúsculas y los espacios')
else:
    print('No ingresaste un palíndromo')
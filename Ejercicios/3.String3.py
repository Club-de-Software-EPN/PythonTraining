# Ejercicio 3
# Validar si los siguientes enlaces son correctos
# https:// y terminar con .com
link1 = 'https://wwww.epn.edu.ec.ecuador'
link2 = 'https://modemat.com'
link3 = 'http:/fis.edu.lat'

# Únicamente se usarán
print('Link 1')
print('Empieza con https ',link1.startswith('https://'))
print('Termina con .com',link1.endswith('.com'))
print('Link 2')
print('Empieza con https ',link2.startswith('https://'))
print('Termina con .com',link2.endswith('.com'))
print('Link 3')
print('Empieza con https ',link3.startswith('https://'))
print('Termina con .com',link3.endswith('.com'))
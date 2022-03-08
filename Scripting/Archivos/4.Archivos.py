# 1. Crear un script que genere un archivo con elemntos repetidos

import random

deportes = ['Futbol','Tenis', 'Basket', 'BalonMano', 'Karate', 'Atletismo']
for i in range(100):
    print(random.choice(deportes))
# Creación archivo desde python
archivo = open('Scripting/Archivos/ejercicio.txt','w')
archivo.close()
# Escribir su contenido
with open('Scripting/Archivos/ejercicio.txt', mode='r+') as miArchivo:    
    for i in range(500):
        miArchivo.write(str(random.choice(deportes)+'\n'))
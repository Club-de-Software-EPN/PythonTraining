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

# Crear un nuevo archiv llamado resumen.txt

# Cabecera 

# Elemento  Ocurrencias
# Furbol    25
# Basket    30


with open('Scripting/Archivos/resumen.txt', mode='w+') as miArchivo:
    contenido = open('Scripting/Archivos/ejercicio.txt','r')
    palabras = contenido.readlines()
    unicas = []
    for palabra in palabras:
        if palabra not in unicas:
            unicas.append(palabra)            
    #['Futbol','Tenis', 'Basket', 'BalonMano', 'Karate', 'Atletismo']       
    ocurrencias = dict((i, palabras.count(i)) for i in unicas)
    print(ocurrencias)
    miArchivo.write('Deporte\t\t\tOcurrencias\n')
    for clave in ocurrencias:
        #print(clave + '  ' + str(ocurrencias[clave]))
        miArchivo.write(str(clave).replace('\n','') + '\t'*3 + str(ocurrencias[clave])+'\n')      
    print(ocurrencias)

    
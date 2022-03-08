# Crear un arhcivo de texto

with open('Scripting/Archivos/ejemplo2.txt', mode='r+') as miArchivo:
    print(miArchivo.read())
    miArchivo.write('Hola')

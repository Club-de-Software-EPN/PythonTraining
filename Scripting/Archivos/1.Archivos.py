# Manejo de los archivos
# Windows texto y binario
# Unix, MacOS: se abre de una única forma

# Modos de tomar un archivo: w,r,a
# En windows:
# wt wb w+
# rt rb r+ = 'read + write'
# at ab a+

miArchivo = open('Scripting/Archivos/ejemplo.txt', 'r')
print(type(miArchivo))
print(miArchivo)
# Como leer un archivo
print(miArchivo.read())
print('--Después--')
# Permite el puntero
miArchivo.seek(0)
print(miArchivo.read())

# Leer varias líneas
print('--Leer varias líneas--')
miArchivo.seek(0)
print(miArchivo.readlines())

miArchivo.close()

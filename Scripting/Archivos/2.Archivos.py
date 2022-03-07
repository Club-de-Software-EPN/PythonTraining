# Manejar archivos con with

with open('Scripting/Archivos/ejemplo.txt', 'r+') as miArchivo:
    # todas las acciones a realziar con el archivo
    print(miArchivo.read())
    # Escribir un archivo
    # write reemplaza el contenido y lo escribe en el archivo
    miArchivo.write('\nTexto escrito desde mi script')
    miArchivo.seek(0)
    print(miArchivo.read())
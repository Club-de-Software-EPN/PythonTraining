# Una función genérica que permita crear una matriz

def crearMatriz():
    matriz = []
    nFilas = int(input('Ingrese el número de filas: '))
    nColumnas = int(input('Ingrese el número de columnas: '))
    for i in range(nFilas):
        matriz.append([0]*nColumnas)
    for i in range(0,nFilas):
        for j in range(0,nColumnas):
            mensaje = f'Ingrese el valor de la fila {i+1} en la columna {j+1}: '
            matriz[i][j] = int(input(mensaje))
    dimensiones = (nFilas,nColumnas)
    return matriz, dimensiones

# Una funcion genérica para imprimir por consola cualquier matriz
def mostrarMatriz(matriz, dimensiones):
    filas, columnas = dimensiones
    for i in range(filas):
        for j in range(columnas):
            print(matriz[i][j], end='\t')
        print('')

def llenarMatriz(matriz, fila, columna):
    matriz[fila-1][columna-1] = 'X'

def main():
    matriz,dimensiones = crearMatriz()    
    mostrarMatriz(matriz, dimensiones)
    llenarMatriz(matriz,2,2)
    print('')
    mostrarMatriz(matriz, dimensiones)

main()
# Una función genérica que permita crear una matriz
from matplotlib.pyplot import table
from sklearn.pipeline import make_union


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
    return matriz

# Una funcion genérica para imprimir por consola cualquier matriz
def mostrarMatriz(matriz, shape):
    pass

def main():
    tablero = crearMatriz()
    print(tablero)

main()
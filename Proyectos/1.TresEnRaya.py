# Tres en raya
# Reglas clásica del tres en línea
# Si tres caracteres son iguales en cualquier sentido se termina e juego
# Van a  existir dos jugadores
# Presentación
# Se pueden asignar nombres a los dos jugadores
# Matriz creada a partir de listas
# Se solicitará que se ingrese la fila y la columna en la que el jugador quiere marcar su movimiento
# Deberá comprobar si se encuentra ocupado perderá el turno
# Se terminará el juego cuando se marque tres en linea
# Se presente un menú al inicio en el que se pueda ingresar los nombre 
# de los jugadores, y adempas escoger los caracteres, por defeco sera la x y e l o
# Y la tercera opción será jugar
# Y la cuarta salir

global nombreJugador1
nombreJugador1 = 'Jugador 1'
global nombreJugador2
nombreJugador2 = 'Jugador 2'
global piezaJugador1
piezaJugador1 = 'X'
global piezaJugador2
piezaJugador2 = 'O'

def crearMatriz():
    matriz = []
    nFilas = 3
    nColumnas = 3
    for i in range(nFilas):
        matriz.append(['-']*nColumnas)
    #for i in range(0,nFilas):
        #for j in range(0,nColumnas):
            #mensaje = f'Ingrese el valor de la fila {i+1} en la columna {j+1}: '
            #matriz[i][j] = int(input(mensaje))
    dimensiones = (nFilas,nColumnas)
    return matriz, dimensiones

def mostrarMatriz(matriz, dimensiones):
    filas, columnas = dimensiones
    for i in range(filas):
        for j in range(columnas):
            print(matriz[i][j], end='\t')
        print('')


def llenarMatriz(matriz, fila, columna, caracter):
    matriz[fila-1][columna-1] = caracter       

def menu():
    print('\n\tTres en raya\n')
    print('1. Nombres jugadores')
    print('2. Cambiar piezas')
    print('3. Jugar')
    print('4. Salir')
    opcion = input('Ingrese una opción: ')
    #print('Dsde adentro de la fun menu:',opcion)
    return opcion

def nombreJugadores():
    print('\n\tNombre jugadores')    
    print('1. Cambiar nombre del jugador 1')
    print('2. Cambiar nombre del jugador 2')
    opcionNombre = input('Cambiar nombre del jugador: ')    
 
    if opcionNombre == '1':
        global nombreJugador1
        nombreJugador1 = input('Nombre del jugador 1: ')        
    elif opcionNombre == '2':
        global nombreJugador2
        nombreJugador2 = input('Nombre del jugador 2: ')
    else:
        print('Ingrese una opción válida')

def cambiarPiezas():
    print('\n\tPiezas')    
    print('1. Cambiar pieza del jugador 1')
    print('2. Cambiar pieza del jugador 2')
    opcionPieza = input('Cambiar pieza del jugador: ')    
    global piezaJugador1
    global piezaJugador2
    if opcionPieza == '1':
        print('Opcion 1')
        auxPieza1 = input('Pieza del jugador 1: ')       
        if  auxPieza1 != piezaJugador2:
            global piezaJugador1   
            piezaJugador1 = auxPieza1
        else:
            print('La pieza ingresada es igual a la del otro jugador')

    elif opcionPieza == '2':
        auxPieza2 = input('Pieza del jugador 2: ')  
        if auxPieza2 != piezaJugador1:            
            piezaJugador2 = auxPieza2
        else:
            print('La pieza ingresada es igual a la del otro jugador')

    else:
        print('Ingrese una opción válida')


def jugar():
    tablero, dimensiones = crearMatriz()
    print('Jugando....')
    print('Es turno del jugador',nombreJugador1)
    print('Es turno del jugador 2',nombreJugador2)
    print('Pieza 1',piezaJugador1)
    print('Pieza 2',piezaJugador2)
    mostrarMatriz(tablero,dimensiones)
    

def mostrarTablero():
    pass

def main():
    terminarJuego = False      
    while terminarJuego == False:
        opcionMenu = menu()  # Va a ejcutar la función menú y tambipne va asignar el retorno a mi variable    
        # Condicionales
        if opcionMenu == '1':
            nombreJugadores()    
        elif opcionMenu == '2':
            cambiarPiezas()
        elif opcionMenu == '3':
            jugar()
        elif opcionMenu == '4':
            print('\tGracias por jugar, te esperamos pronto')
            terminarJuego = True
        else:
            print('Por favor ingrese una opción válida')             

main()
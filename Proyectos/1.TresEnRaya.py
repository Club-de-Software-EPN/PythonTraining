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
        nombreJugador1 = input('Nombre del jugador 1: ')

def jugar():
    print('Jugando....')
    print('Es turno del jugador',nombreJugador1)

def mostrarTablero():
    pass

def main():
    opcionMenu = menu()  # Va a ejcutar la función menú y tambipne va asignar el retorno a mi variable
    
    # Condicionales
    if opcionMenu == '1':
       nombreJugadores()    
    elif opcionMenu == '2':
        print('Cambiar piezas')
    elif opcionMenu == '3':
        jugar()
    elif opcionMenu == '4':
        print('Saliendo')
    else:
        print('Por favor ingrese una opción válida')
    
    jugar()

main()
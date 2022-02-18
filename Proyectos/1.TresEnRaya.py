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

def menu():
    print('\n\tTres en raya\n')
    print('1. Nombres jugadores')
    print('2. Cambiar piezas')
    print('3. Jugar')
    print('4. Salir')
    opcion = input('Ingrese una opción: ')
    #print('Dsde adentro de la fun menu:',opcion)
    return opcion


def mostrarTablero():
    pass

def main():
    opcionMenu = menu()  # Va a ejcutar la función menú y tambipne va asignar el retorno a mi variable
    # Condicionales
    if opcionMenu == '1':
        print('Submenu ingresa los nombre')
    

main()
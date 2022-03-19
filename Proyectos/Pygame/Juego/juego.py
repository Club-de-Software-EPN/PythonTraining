from weakref import finalize
import pygame

dimensionesPantalla = (600,500)
colorFondo = (215, 255, 54)

# Inicialización de una instancia pygame
pygame.init()

# Configuraciones juego
pygame.display.set_caption('Monstruos')

# Creando una pantalla de juego
screen = pygame.display.set_mode(dimensionesPantalla)

# Bucle principal del juego
finalizado = False

while not finalizado:
    # Escenografía básica
    screen.fill(colorFondo)

    # Elementos dinámicos
    

    # Eventos (gestor de eventos de pygame)
    for event in pygame.event.get():
        # Evento cerrar una ventana
        if event.type == pygame.QUIT:
            finalizado = True

    # Actualizar la pantalla
    pygame.display.update()
